from PySide2.QtCore import Slot
from PySide2.QtWidgets import QWidget, QLabel, QProgressBar

from app.lib.proxy_checker.statistics.proxy_checker_statistics import ProxyCheckerStatistics


class StatisticsWidget(QWidget):
    __statistics = None

    @property
    def statistics(self):
        return self.__statistics

    @statistics.setter
    def statistics(self, statistics: ProxyCheckerStatistics):
        self.__statistics = statistics
        statistics.update_statistics_signal.connect(self.update_progress_statistics)

    @Slot(object)
    def update_progress_statistics(self, statistics: ProxyCheckerStatistics):
        self.parent().findChild(QLabel, "good_http").setText(str(statistics.good_http()))
        self.parent().findChild(QLabel, "good_socks4").setText(str(statistics.good_socks4()))
        self.parent().findChild(QLabel, "good_socks5").setText(str(statistics.good_socks5()))
        self.parent().findChild(QLabel, "total_bad_proxy").setText(str(statistics.bad_proxy()))
        self.parent().findChild(QLabel, "total_good_proxy").setText(str(statistics.good_proxy()))
        self.update_progress_bar(statistics)

    def update_progress_bar(self, statistics: ProxyCheckerStatistics):
        progressBar = self.parent().findChild(QProgressBar, "progressBar")
        progressBar.setMaximum(statistics.total())
        progressBar.setValue(statistics.passed())
        progressBar.setFormat('{}% ({} / {})'.format(
            str(statistics.progress_in_percent()),
            str(statistics.passed()),
            str(statistics.total())
        ))

    def clear_statistics(self):
        self.update_progress_statistics(ProxyCheckerStatistics())
        progressBar = self.parent().findChild(QProgressBar, "progressBar")
        progressBar.setFormat("0%")
        progressBar.setValue(0)
        progressBar.setMaximum(1)
