from PySide2.QtCore import QObject, Signal, Slot

from lib.proxy.proxy import Proxy


class ProxyStorage(QObject):
    update_statistics_signal = Signal(object)

    def __init__(self):
        super().__init__()
        self.proxies = list()

    def import_from_file(self, file, proxy_type):
        proxy_type = str(proxy_type).lower().strip()
        with open(file, "r", encoding='utf8') as file:
            for line in file.readlines():
                self.proxies.append(Proxy(line, proxy_type))
        self.update_statistics_signal.emit(self)

    def clear(self):
        self.proxies.clear()
        self.update_statistics_signal.emit(self)

    def socks4(self) -> list:
        return list(filter(lambda proxy: proxy.proxy_type == 'socks4', self.proxies))

    def socks5(self) -> list:
        return list(filter(lambda proxy: proxy.proxy_type == 'socks5', self.proxies))

    def http(self) -> list:
        return list(filter(lambda proxy: proxy.proxy_type == 'http', self.proxies))

    @Slot()
    def clear_socks4(self):
        for proxy in self.socks4():
            self.proxies.remove(proxy)
        self.update_statistics_signal.emit(self)

    @Slot()
    def clear_socks5(self):
        for proxy in self.socks5():
            self.proxies.remove(proxy)
        self.update_statistics_signal.emit(self)

    @Slot()
    def clear_http(self):
        for proxy in self.http():
            self.proxies.remove(proxy)
        self.update_statistics_signal.emit(self)

    def total(self):
        return self.total_http() + self.total_socks4() + self.total_socks5()

    def total_http(self):
        return len(self.http())

    def total_socks4(self):
        return len(self.socks4())

    def total_socks5(self):
        return len(self.socks5())

    def is_empty(self):
        return self.total() == 0
