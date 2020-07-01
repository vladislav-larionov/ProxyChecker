
class Proxy:
    @staticmethod
    def http(proxy: str):
        return Proxy(proxy.strip(), 'http')

    @staticmethod
    def socks5(proxy: str):
        return Proxy(proxy.strip(), 'socks5')

    @staticmethod
    def socks4(proxy: str):
        return Proxy(proxy.strip(), 'socks4')

    def __init__(self, proxy, proxy_type=None):
        self.proxy = str(proxy).strip()
        self.proxy_type = str(proxy_type)

    def __str__(self):
        return self.proxy

    def to_http_protocols(self):
        return {
            'http': '{}://{}'.format(self.proxy_type, self.proxy),
            'https': '{}://{}'.format(self.proxy_type, self.proxy)
        }


class ProxyNullObject:
    def to_http_protocols(self):
        return None
