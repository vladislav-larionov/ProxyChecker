import time

from PySide2.QtCore import QObject, Signal, QThread


class ProxyCheckerConnection(QObject):
    valid_proxy_signal = Signal(int, int, int)
    done_signal = Signal()


class ProxyChecker(QThread):
    signals = ProxyCheckerConnection()

    def __init__(self, url="https://mail.ru", http_proxies=None, socks4_proxies=None, socks5_proxies=None):
        super().__init__()
        if socks5_proxies is None:
            socks5_proxies = set()
        if socks4_proxies is None:
            socks4_proxies = set()
        if http_proxies is None:
            http_proxies = set()
        self.__url = url
        self.__proxies = list()
        self.__proxies.extend(self.__proxy_list_to_hash_list(socks5_proxies, 'socks5'))
        self.__proxies.extend(self.__proxy_list_to_hash_list(socks4_proxies, 'socks4'))
        self.__proxies.extend(self.__proxy_list_to_hash_list(http_proxies, 'http'))
        self.__good_proxy_counts = {'socks4': 0, 'socks5': 0, 'http': 0}
        self.__good_proxies_files = {
            'socks4': open("socks4.txt", "w"),
            'socks5': open("socks5.txt", "w"),
            'http': open("http.txt", "w")
        }

    @classmethod
    def __proxy_list_to_hash_list(cls, proxies, proxy_type):
        return map(lambda proxy: {'type': proxy_type, 'proxy': proxy}, proxies)

    def start_check(self):
        for proxy in self.__proxies:
            if True:
                self.__good_proxy_counts[proxy['type']] += 1
                self.__write_to_file(proxy)
                self.signals.valid_proxy_signal.emit(
                    self.__good_proxy_counts['http'],
                    self.__good_proxy_counts['socks4'],
                    self.__good_proxy_counts['socks5']
                )

    @classmethod
    def __write_to_file(cls, proxy):
        with open("{proxy_type}.txt".format(proxy_type=proxy['type']), "a") as proxy_file:
            proxy_file.write(proxy['proxy'])
            proxy_file.write("\n")

    def run(self):
        self.start_check()
        self.signals.done_signal.emit()
