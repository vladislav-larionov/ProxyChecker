import requests

from requests import ConnectTimeout, ReadTimeout, ConnectionError
from requests.exceptions import ProxyError, ChunkedEncodingError

# from urllib3 import disable_warnings, exceptions
#
# disable_warnings(exceptions.InsecureRequestWarning)
from socks import GeneralProxyError
from urllib3.exceptions import MaxRetryError


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
            print(self.__response.status_code)
            return self.__response.ok
        except (ConnectTimeout, ReadTimeout, ProxyError, ConnectionError) as e:
            print("{}, error: {}".format(self.__proxy, type(e)))
            return False
        except ChunkedEncodingError as e:
            print("{}, error: {}".format(self.__proxy, type(e)))
            return False

    @classmethod
    def __proxy_to_http_protocols_hash(cls, proxy):
        return {
            'http': '{}://{}'.format(proxy['type'], proxy["proxy"]),
            'https': '{}://{}'.format(proxy['type'], proxy["proxy"])
        }

# responce = Request(
#     url='https://mail.ru',
#     proxy={'type': 'http', 'proxy': '94.130.179.24:8045'}
# ).do_request()
#
# # proxy = {'http': 'http://185.59.213.253:8081', 'https': 'https://185.59.213.253:8081'}
# print(responce)
