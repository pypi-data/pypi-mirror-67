# coding=utf8
import os
import logging
import socket
import Ice
# It's not wrong here
from cma.cimiss import stub_ice
import cma
import xarray as xr
import pandas as pd
import numpy as np
import urllib3
from urllib.parse import urlparse
from pathlib import Path
# typing
from typing import Optional
from typing import Dict
from typing import List
from typing import Union

logger = logging.getLogger('cimiss_python')

_http = urllib3.PoolManager()


class RequestError(Exception):
    def __init__(self, error_info: str):
        self.error_info = error_info

    def __str__(self) -> str:
        return self.error_info


class Query(Ice.Application):

    def __init__(self, user_id: str, password: str, host: str, port: int = 1888,
                 config_file: Optional[str] = None):

        super().__init__()
        ice_file_path = os.path.join(os.path.dirname(stub_ice.__file__), 'stub.ice')
        Ice.loadSlice(ice_file_path)
        init_data = Ice.InitializationData()
        init_data.properties = Ice.createProperties()

        if config_file:
            init_data.properties.load(config_file)
            logger.debug(f'load initial config from file: {config_file}')
            self._ic = Ice.initialize(init_data)
            base = self._ic.stringToProxy(init_data.properties.getProperty("DataApi.Proxy"))
        else:
            logger.debug('load default initial config')
            init_data.properties.setProperty("Ice.Warn.Connections", "1")
            init_data.properties.setProperty("Ice.Trace.Protocol", "0")
            init_data.properties.setProperty("Ice.MessageSizeMax", "20971520")
            init_data.properties.setProperty("Ice.ThreadPool.Client.Size", "10")
            init_data.properties.setProperty("Ice.Default.EncodingVersion", "1.0")
            self._ic = Ice.initialize(init_data)
            base = self._ic.stringToProxy(f"DataApi:tcp -h {host} -p {port}")

        self._api = cma.cimiss.DataAPIAccessPrx.checkedCast(base)

        if not self._api:
            raise RuntimeError("Invalid proxy")
        self._client_ip = socket.gethostbyname(socket.gethostname())
        self._language = "python"
        self._version = "1.3"
        self._user_id = user_id
        self._pwd = password
        self._host = host
        self._port = port

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.destroy()

    def destroy(self):
        self._ic.destroy()

    def array_2d(self, interface_id: str, params: Dict[str, str],
                 dtypes: Optional[Dict[str, Union[str, np.dtype]]] = None) -> pd.DataFrame:

        resp = self._api.callAPItoarray2D(self._user_id, self._pwd,
                                          interface_id, self._client_ip, self._language, self._version,
                                          params)
        if resp.request.errorCode != 0:
            raise RequestError(resp.request.errorMessage)
        logger.debug(resp.request.errorMessage)
        elements = resp.request.requestElems.split(',')
        data = resp.data

        df = pd.DataFrame(data, columns=elements)
        if dtypes is not None:
            df = df.astype(dtypes)
        return df

    def grid_array_2d(self, interface_id: str, params: Dict[str, str]) -> xr.DataArray:
        resp = self._api.callAPItogridArray2D(self._user_id, self._pwd,
                                              interface_id, self._client_ip, self._language,
                                              self._version,
                                              params)
        if resp.request.errorCode != 0:
            raise RequestError(resp.request.errorMessage)
        logger.debug(resp.request.errorMessage)
        lat = np.linspace(resp.startLat, resp.endLat, resp.latCount)
        lon = np.linspace(resp.startLon, resp.endLon, resp.lonCount)
        da = xr.DataArray(resp.data, coords=[('lat', lat), ('lon', lon)])
        return da

    def _redir_host(self, url: str, follow_host: Union[bool, str]) -> str:
        if not url.startswith('http'):
            url = 'http://' + url
        if follow_host is True:
            url = urlparse(url)._replace(netloc=self._host).geturl()
        elif isinstance(follow_host, str):
            url = urlparse(url)._replace(netloc=follow_host).geturl()
        return url

    def save_file(self, interface_id: str,
                  params: Dict[str, str],
                  data_format: str,
                  file_name: Union[str, Path],
                  follow_host: Union[bool, str] = False
                  ) -> str:
        file_name = Path(file_name)
        if file_name.is_dir():
            raise IOError('[{}] is a directory'.format(str(file_name)))

        resp = self._api.callAPItosaveAsFile(self._user_id, self._pwd,
                                             interface_id, self._client_ip, self._language, self._version,
                                             params, data_format, file_name.name)
        if resp.request.errorCode != 0:
            raise RequestError(resp.request.errorMessage)
        logger.debug(resp.request.errorMessage)

        url: str = self._redir_host(resp.fileInfos[0].fileUrl, follow_host)
        response = _http.request('GET', url)
        with open(file_name, 'wb') as f:
            f.write(response.data)
        return file_name

    def file_list(self, interface_id: str, params: Dict[str, str]) -> pd.DataFrame:
        resp = self._api.callAPItofileList(self._user_id, self._pwd,
                                           interface_id, self._client_ip, self._language, self._version,
                                           params)
        if resp.request.errorCode != 0:
            raise RequestError(resp.request.errorMessage)
        logger.debug(resp.request.errorMessage)
        file_infos = list(map(lambda x: x.__dict__, resp.fileInfos))
        df = pd.DataFrame.from_records(file_infos)
        return df

    def down_file(self, interface_id: str,
                  params: Dict[str, str],
                  file_dir: Union[str, Path],
                  follow_host: Union[bool, str] = False
                  ) -> List[str]:
        file_dir = Path(file_dir)
        resp = self._api.callAPItofileList(self._user_id, self._pwd,
                                           interface_id, self._client_ip, self._language, self._version,
                                           params)
        if resp.request.errorCode != 0:
            raise RequestError(resp.request.errorMessage)
        logger.debug(resp.request.errorMessage)

        if not file_dir.exists():
            file_dir.mkdir()

        downloaded: List[str] = []
        for i, info in enumerate(resp.fileInfos):
            logger.info(f'downloading file {i + 1}/{len(resp.fileInfos)} ...')

            url: str = self._redir_host(info.fileUrl, follow_host)
            response = _http.request('GET', url)
            with open(file_dir / info.fileName, 'wb') as f:
                f.write(response.data)
            downloaded.append(info.fileName)
        return downloaded

    def serialized_str(self, interface_id: str, params: Dict[str, str], data_format: str) -> str:
        result = self._api.callAPItoserializedStr(self._user_id, self._pwd,
                                                  interface_id, self._client_ip, self._language, self._version,
                                                  params, data_format)
        return result

    def store_array_2d(self, interface_id: str, params: Dict[str, str], in_array_2d: List[List[str]]):
        result = self._api.callAPItostoreArray2D(self._user_id, self._pwd,
                                                 interface_id, self._client_ip, self._language, self._version,
                                                 params, in_array_2d)
        return result

    def store_file_by_ftp(self, interface_id: str, params: Dict[str, str], in_array_2d, ftp_files: str):
        result = self._api.callAPItostoreFileByFtp(self._user_id, self._pwd,
                                                   interface_id, self._client_ip, self._language, self._version,
                                                   params, in_array_2d, ftp_files)
        return result

    def store_serialized_str(self, interface_id: str, params: Dict[str, str], in_string: str):
        result = self._api.callAPItostoreSerializedStr(self._user_id, self._pwd,
                                                       interface_id, self._client_ip, self._language, self._version,
                                                       params, in_string)
        return result
