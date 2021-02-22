from PySide2.QtCore import QObject, Signal


class ProxyCheckerStatistics(QObject):
    update_statistics_signal = Signal(object)

    def __init__(self, total=0):
        super().__init__()
        self.__total = total
        self.__passed = 0
        self.__good_proxy = {'socks4': 0, 'socks5': 0, 'http': 0}
        self.__bad = 0

    def good_socks4(self):
        return self.__good_proxy['socks4']

    def good_socks5(self):
        return self.__good_proxy['socks5']

    def good_http(self):
        return self.__good_proxy['http']

    def total(self):
        return self.__total

    def passed(self):
        return self.__passed

    def bad_proxy(self):
        return self.__bad

    def good_proxy(self):
        return self.good_socks5() + self.good_socks4() + self.good_http()

    def increase_good(self, proxy_type: str):
        self.__good_proxy[proxy_type] += 1
        self.update_statistics_signal.emit(self)

    def increase_bad(self):
        self.__bad += 1
        self.update_statistics_signal.emit(self)

    def increase_socks4(self):
        self.__good_proxy['socks4'] += 1
        self.update_statistics_signal.emit(self)

    def increase_socks5(self):
        self.__good_proxy['socks5'] += 1
        self.update_statistics_signal.emit(self)

    def increase_http(self):
        self.__good_proxy['http'] += 1
        self.update_statistics_signal.emit(self)

    def progress_in_percent(self):
        if self.__total == 0:
            return 0
        return round(self.__passed / self.__total * 100)

    def increase_passed(self):
        self.__passed += 1
        self.update_statistics_signal.emit(self)

    def emit_update_statistics_signal(self):
        self.update_statistics_signal.emit(self)
