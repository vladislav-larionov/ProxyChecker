from PySide2.QtCore import QObject, Signal, Slot


class ProxyStorage(QObject):
    update_statistics_signal = Signal(object)

    def __init__(self):
        super().__init__()
        self.__proxies = {'socks4': set(), 'socks5': set(), 'http': set()}

    def __import_proxy(self, proxy, collection, file, proxy_type):
        if collection is not None:
            self.__import_from_collection(collection, proxy_type)
        if file is not None:
            self.__import_from_file(file, proxy_type)
        if proxy is not None:
            self.__proxies[proxy_type].update(proxy)
        self.update_statistics_signal.emit(self)

    def __import_from_collection(self, collection, proxy_type):
        self.__proxies[proxy_type].update(self.__strip_proxy(collection))

    def __import_from_file(self, file, proxy_type):
        with open(file, "r", encoding='utf8') as file:
            self.__proxies[proxy_type].update(self.__strip_proxy(file.readlines()))

    def import_socks4(self, proxy=None, collection=None, file=None):
        self.__import_proxy(proxy, collection, file, 'socks4')

    def import_socks5(self, proxy=None, collection=None, file=None):
        self.__import_proxy(proxy, collection, file, 'socks5')

    def import_http(self, proxy=None, collection=None, file=None):
        self.__import_proxy(proxy, collection, file, 'http')

    def clear(self):
        self.__proxies['socks4'].clear()
        self.__proxies['socks5'].clear()
        self.__proxies['http'].clear()
        self.update_statistics_signal.emit(self)

    @Slot()
    def clear_socks4(self):
        self.__proxies['socks4'].clear()
        self.update_statistics_signal.emit(self)

    @Slot()
    def clear_socks5(self):
        self.__proxies['socks5'].clear()
        self.update_statistics_signal.emit(self)

    @Slot()
    def clear_http(self):
        self.__proxies['http'].clear()
        self.update_statistics_signal.emit(self)

    @classmethod
    def __strip_proxy(cls, proxy_list):
        return map(lambda proxy: proxy.strip(), proxy_list)

    def total(self):
        return self.total_http() + self.total_socks4() + self.total_socks5()

    def total_http(self):
        return len(self.__proxies['http'])

    def total_socks4(self):
        return len(self.__proxies['socks4'])

    def total_socks5(self):
        return len(self.__proxies['socks5'])

    def to_hash_list(self):
        return list(map(lambda proxy: {'type': 'socks4', 'proxy': proxy}, self.__proxies['socks4'])) + list(
            map(lambda proxy: {'type': 'socks5', 'proxy': proxy}, self.__proxies['socks5'])) + list(
            map(lambda proxy: {'type': 'http', 'proxy': proxy}, self.__proxies['http']))

    def empty(self):
        return self.total() == 0
