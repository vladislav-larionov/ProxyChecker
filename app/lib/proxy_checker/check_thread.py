import sys

from PySide2.QtCore import QThread, QObject, Signal

from app.lib.proxy.proxy import Proxy
from app.lib.proxy_checker.data_storage import DataStorage
from app.lib.proxy_checker.request import Request


class Signals(QObject):
    valid_signal = Signal(object)
    invalid_signal = Signal(object)
    thread_done_signal = Signal()


class CheckThread(QThread):
    def __init__(self, storage: DataStorage, url, timeout):
        super().__init__()
        self.storage = storage
        self.signals = Signals()
        self.url = url
        self.timeout = timeout
        self.current_proxy = None

    def run(self):
        try:
            while self.storage.has_next():
                self.current_proxy = self.storage.next()
                self.check_proxy(self.current_proxy)
            self.signals.thread_done_signal.emit()
        except Exception as e:
            print(e, file=sys.stderr)

    def check_proxy(self, proxy: Proxy):
        result = Request(url=self.url, proxy=proxy, timeout=self.timeout).do_request()
        if result:
            self.signals.valid_signal.emit(proxy)
        else:
            self.signals.invalid_signal.emit(proxy)

    def revert_current_data(self):
        self.storage.add(self.current_proxy)
