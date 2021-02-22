
from PySide2.QtCore import QObject, Signal, Slot

from app.lib.proxy_checker.ThreadPool import ThreadPool
from app.lib.proxy_checker.check_thread import CheckThread
from app.lib.proxy_checker.data_storage import DataStorage
from app.lib.proxy_checker.project.project import Project
from app.lib.proxy_storage.proxy_storage import ProxyStorage

from app.lib.proxy_checker.statistics.proxy_checker_statistics import ProxyCheckerStatistics


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
        self.thread_pool = ThreadPool()
        for _i in range(thread_count):
            thread = CheckThread(self.__storage, url, timeout)
            thread.signals.valid_signal.connect(self.on_valid_signal)
            thread.signals.invalid_signal.connect(self.on_invalid_signal)
            self.thread_pool.add_thread(thread)
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
