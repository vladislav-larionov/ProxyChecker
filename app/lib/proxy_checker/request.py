import requests

from requests import ConnectTimeout, ReadTimeout, ConnectionError, Response
from requests.exceptions import ProxyError, ChunkedEncodingError, MissingSchema

from app.lib.proxy.proxy import Proxy, ProxyNullObject


class Request:
    def __init__(self, url, proxy: Proxy = ProxyNullObject(), timeout=3):
        self.__proxy = proxy.to_http_protocols()
        self.__url = url
        self.__timeout = timeout
        self.__headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0',
            'Accept-Encoding': 'gzip, deflate',
            'Accept': '*/*',
            'Connection': 'keep-alive'
        }
        self.__response = None

    def do_request(self) -> Response:
        try:
            self.__response = requests.get(self.__url, proxies=self.__proxy, timeout=self.__timeout,
                                           headers=self.__headers)
            return self.__response
        except (ConnectTimeout, ReadTimeout, ProxyError, ConnectionError) as _e:
            return self.__response
        except ChunkedEncodingError as _e:
            return self.__response
        except MissingSchema as _e:
            return self.__response
