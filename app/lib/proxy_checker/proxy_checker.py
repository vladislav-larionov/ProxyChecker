
from PySide2.QtCore import QObject, Signal, Slot

from lib.proxy_checker.ThreadPool import ThreadPool
from lib.proxy_checker.check_thread import CheckThread
from lib.proxy_checker.data_storage import DataStorage
from lib.proxy_checker.project import Project
from lib.proxy_checker.proxy_checker_statistics import ProxyCheckerStatistics
from lib.proxy_storage.proxy_storage import ProxyStorage


class ProxyCheckerConnection(QObject):
    done_signal = Signal()
    stop_signal = Signal()


class ProxyChecker(QObject):
    signals = ProxyCheckerConnection()

    def __init__(self, proxy_storage: ProxyStorage, url, timeout=1, thread_count=1):
        super().__init__()
        self.timeout = timeout
        self.__storage = DataStorage(proxy_storage.proxies)
        self.__statistics = ProxyCheckerStatistics(proxy_storage.total())
        self.__project = Project()
        self.thread_pool = ThreadPool(int(thread_count))
        for thread in self.thread_pool.init_threads(CheckThread, self.__storage):
            thread.url = url
            thread.timeout = int(timeout)
            thread.signals.valid_signal.connect(self.on_valid_signal)
            thread.signals.invalid_signal.connect(self.on_invalid_signal)
        self.thread_pool.done_signal.connect(self.on_done_signal)

    @property
    def statistics(self):
        return self.__statistics

    def project_path(self):
        return self.__project.project_path

    def run(self):
        self.thread_pool.start()

    @Slot()
    def on_valid_signal(self, proxy):
        self.__statistics.increase_good(proxy.proxy_type)
        self.__project.store_good_proxy(proxy)
        self.__statistics.increase_passed()

    @Slot()
    def on_invalid_signal(self, proxy):
        self.__statistics.increase_bad()
        self.__statistics.increase_passed()

    @Slot()
    def on_done_signal(self):
        self.signals.done_signal.emit()

    def stop(self):
        self.thread_pool.stop()
        self.signals.done_signal.emit()
