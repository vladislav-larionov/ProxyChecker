from concurrent.futures import wait
from concurrent.futures.thread import ThreadPoolExecutor

from PySide2.QtCore import QObject, Signal, QThread

from lib.proxy_checker_statistics import ProxyCheckerStatistics
from lib.request import Request


class ProxyCheckerConnection(QObject):
    done_signal = Signal()


class ProxyChecker(QThread):
    signals = ProxyCheckerConnection()

    def __init__(self, url="https://mail.ru", http_proxies=None, socks4_proxies=None, socks5_proxies=None, timeout=1,
                 threads=1):
        super().__init__()
        if socks5_proxies is None:
            socks5_proxies = set()
        if socks4_proxies is None:
            socks4_proxies = set()
        if http_proxies is None:
            http_proxies = set()
        self.__url = url
        self.__timeout = timeout
        self.__threads = threads
        self.__thread_pool = ThreadPoolExecutor(max_workers=self.__threads)
        self.__futures = list()
        self.__proxies = list()
        self.__proxies.extend(self.__proxy_list_to_hash_list(socks5_proxies, 'socks5'))
        self.__proxies.extend(self.__proxy_list_to_hash_list(socks4_proxies, 'socks4'))
        self.__proxies.extend(self.__proxy_list_to_hash_list(http_proxies, 'http'))
        self.__statistics = ProxyCheckerStatistics(len(self.__proxies))
        self.__good_proxies_files = {
            'socks4': open("socks4.txt", "w"),
            'socks5': open("socks5.txt", "w"),
            'http': open("http.txt", "w")
        }

    @property
    def statistics(self):
        return self.__statistics

    @classmethod
    def __proxy_list_to_hash_list(cls, proxies, proxy_type):
        return map(lambda proxy: {'type': proxy_type, 'proxy': proxy}, proxies)

    def start_check(self):
        with self.__thread_pool:
            for proxy in self.__proxies:
                self.__futures.append(self.__thread_pool.submit(self.__check_proxy, proxy))

    def __check_proxy(self, proxy):
        if True:
            self.__statistics.increase_good(proxy['type'])
            self.__write_to_file(proxy)
        else:
            self.__statistics.increase_bad()
        self.__statistics.increase_passed()

    @classmethod
    def __write_to_file(cls, proxy):
        with open("{proxy_type}.txt".format(proxy_type=proxy['type']), "a") as proxy_file:
            proxy_file.write(proxy['proxy'])
            proxy_file.write("\n")

    def run(self):
        self.start_check()
        self.signals.done_signal.emit()

    def stop(self):
        self.__stop_worker_thread()
        self.__stop_main_thread()
        self.signals.done_signal.emit()

    def __stop_main_thread(self):
        self.terminate()
        self.wait()

    def __stop_worker_thread(self):
        self.__thread_pool.shutdown(wait=False)
        for future in self.__futures:
            future.cancel()
        wait(self.__futures)
