import requests

from requests import ConnectTimeout, ReadTimeout, ConnectionError
from requests.exceptions import ProxyError, ChunkedEncodingError


class Request:
    def __init__(self, url, proxy=None, timeout=3):
        if proxy:
            self.__proxy = self.__proxy_to_http_protocols_hash(proxy)
        else:
            self.__proxy = proxy
        self.__url = url
        self.__timeout = timeout
        self.__headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0',
            'Accept-Encoding': 'gzip, deflate',
            'Accept': '*/*',
            'Connection': 'keep-alive'
        }
        self.__response = None

    def do_request(self):
        try:
            self.__response = requests.get(self.__url, proxies=self.__proxy, timeout=self.__timeout,
                                           headers=self.__headers)
            return self.__response.ok
        except (ConnectTimeout, ReadTimeout, ProxyError, ConnectionError) as e:
            return False
        except ChunkedEncodingError as e:
            return False

    @classmethod
    def __proxy_to_http_protocols_hash(cls, proxy):
        return {
            'http': '{}://{}'.format(proxy['type'], proxy["proxy"]),
            'https': '{}://{}'.format(proxy['type'], proxy["proxy"])
        }
