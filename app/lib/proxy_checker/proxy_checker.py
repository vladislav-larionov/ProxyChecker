import os
from datetime import datetime
from concurrent.futures import wait
from concurrent.futures.thread import ThreadPoolExecutor
from os.path import normpath, join

from PySide2.QtCore import QObject, Signal, QThread

from lib.proxy.proxy import Proxy
from lib.proxy_checker.proxy_checker_statistics import ProxyCheckerStatistics
from lib.proxy_checker.request import Request
from lib.proxy_storage.proxy_storage import ProxyStorage


class ProxyCheckerConnection(QObject):
    done_signal = Signal()


class ProxyChecker(QThread):
    signals = ProxyCheckerConnection()

    def __init__(self, proxy_storage: ProxyStorage, url, timeout=1, threads=1):
        super().__init__()
        self.__url = url
        self.__timeout = int(timeout)
        self.__thread_pool = ThreadPoolExecutor(max_workers=int(threads))
        self.__futures = list()
        self.__proxy_storage = proxy_storage
        self.__statistics = ProxyCheckerStatistics(proxy_storage.total())
        self.__project_path = self.__create_project_directory()

    @classmethod
    def __create_project_directory(cls):
        project_path = normpath(join(os.getcwd(), datetime.now().strftime('Project [%d_%m_%Y]/Results [%H_%M_%S]')))
        os.makedirs(project_path)
        return project_path

    @property
    def statistics(self):
        return self.__statistics

    @property
    def project_path(self):
        return self.__project_path

    def __start_check(self):
        with self.__thread_pool:
            for proxy in self.__proxy_storage.proxies:
                self.__futures.append(self.__thread_pool.submit(self.__check_proxy, proxy))

    def __check_proxy(self, proxy: Proxy):
        if Request(url=self.__url, proxy=proxy, timeout=self.__timeout).do_request():
            self.__statistics.increase_good(proxy.proxy_type)
            self.__write_to_file(proxy)
        else:
            self.__statistics.increase_bad()
        self.__statistics.increase_passed()

    def __write_to_file(self, proxy: Proxy):
        with open("{project_path}\{proxy_type}.txt".format(project_path=self.project_path, proxy_type=proxy.proxy_type),
                  "a") as proxy_file:
            proxy_file.write(str(proxy))
            proxy_file.write("\n")

    def run(self):
        self.__start_check()
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
