# pylint: disable=R0902
"""
Main window of the app
"""
import os

from PySide2.QtCore import Slot, SIGNAL, QThread
from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox

from lib.proxy_checker.proxy_checker import ProxyChecker
from lib.proxy_checker.proxy_checker_statistics import ProxyCheckerStatistics
from lib.proxy_storage.proxy_storage import ProxyStorage
from ui.forms.main_window_form import Ui_MainWindow


class MainWindow(QMainWindow):
    """
    Class that describes main window of the app
    """

    def signals(self, main_window_ui):
        """ Connect signals from ui """
        self.connect(main_window_ui.import_http, SIGNAL("clicked()"), self.import_http_form_file)
        self.connect(main_window_ui.import_socks4, SIGNAL("clicked()"), self.import_socks4_form_file)
        self.connect(main_window_ui.import_socks5, SIGNAL("clicked()"), self.import_socks5_form_file)
        self.connect(main_window_ui.clear_http, SIGNAL("clicked()"), self.__proxy_storage.clear_http)
        self.connect(main_window_ui.clear_socks4, SIGNAL("clicked()"), self.__proxy_storage.clear_socks4)
        self.connect(main_window_ui.clear_socks5, SIGNAL("clicked()"), self.__proxy_storage.clear_socks5)
        self.connect(main_window_ui.start_btn, SIGNAL("clicked()"), self.start_check)
        self.connect(main_window_ui.stop_btn, SIGNAL("clicked()"), self.stop_check)
        self.connect(main_window_ui.reset_button, SIGNAL("clicked()"), self.reset)
        self.connect(main_window_ui.home_directory, SIGNAL("triggered()"), self.open_home_directory)
        self.__proxy_storage.update_statistics_signal.connect(self.update_import_statistics)
        self.main_window_ui.import_http.signals.file_dropped.connect(self.import_proxy_form_drag_and_drop)
        self.main_window_ui.import_socks4.signals.file_dropped.connect(self.import_proxy_form_drag_and_drop)
        self.main_window_ui.import_socks5.signals.file_dropped.connect(self.import_proxy_form_drag_and_drop)

    @Slot()
    def open_home_directory(self):
        if self.__proxy_checker is None:
            os.startfile(os.getcwd())
        else:
            os.startfile(self.__proxy_checker.project_path())

    def __init__(self):
        """ Constructor of widget """
        main_window = QMainWindow()
        self.main_window_ui = Ui_MainWindow()
        self.main_window_ui.setupUi(main_window)
        QMainWindow.__init__(self)
        Ui_MainWindow.setupUi(self.main_window_ui, self)
        self.__proxy_storage = ProxyStorage()
        self.__proxy_checker = None
        self.signals(self.main_window_ui)

    @Slot()
    def import_http_form_file(self):
        for file_path in self.__open_proxy_file_dialog():
            self.__proxy_storage.import_from_file(file_path, 'http')

    @Slot()
    def import_socks4_form_file(self):
        for file_path in self.__open_proxy_file_dialog():
            self.__proxy_storage.import_from_file(file_path, 'socks4')

    @Slot()
    def import_socks5_form_file(self):
        for file_path in self.__open_proxy_file_dialog():
            self.__proxy_storage.import_from_file(file_path, 'socks5')

    def __open_proxy_file_dialog(self):
        file_name = QFileDialog.getOpenFileName(self, dir=self.tr("./"), filter=self.tr("*.txt"))
        if file_name[0]:
            yield file_name[0]

    @Slot(str, str)
    def import_proxy_form_drag_and_drop(self, file_path, proxy_type):
        self.__proxy_storage.import_from_file(file_path, proxy_type)

    @Slot(object)
    def update_import_statistics(self, storage: ProxyStorage):
        self.main_window_ui.http_count.setText(str(storage.total_http()))
        self.main_window_ui.socks4_count.setText(str(storage.total_socks4()))
        self.main_window_ui.socks5_count.setText(str(storage.total_socks5()))
        self.main_window_ui.total_proxy_loaded.setText(str(storage.total()))

    @Slot()
    def start_check(self):
        if self.__proxy_storage.is_empty():
            QMessageBox.information(self, "Information", "Proxies are not loaded")
            return
        if self.threads() > self.__proxy_storage.total():
            self.set_threads(self.__proxy_storage.total())
        self.__set_start_mode(True)

        self.__proxy_checker = self.init_proxy_checker()
        self.update_progress_statistics(self.__proxy_checker.statistics)

        self.thread = QThread()
        self.__proxy_checker.moveToThread(self.thread)
        self.thread.started.connect(self.__proxy_checker.run)
        self.thread.start()

    def init_proxy_checker(self):
        proxy_checker = ProxyChecker(self.__proxy_storage, self.__get_url(), self.__timeout(), self.threads())
        proxy_checker.statistics.update_statistics_signal.connect(self.update_progress_statistics)
        proxy_checker.signals.done_signal.connect(self.done_check)
        return proxy_checker

    @Slot()
    def done_check(self):
        self.__set_start_mode(False)
        self.__proxy_checker.signals.done_signal.disconnect()
        self.thread.terminate()

    @Slot()
    def stop_check(self):
        self.main_window_ui.stop_btn.setEnabled(False)
        self.__proxy_checker.stop()

    def __timeout(self):
        return int(self.main_window_ui.timeout.text())

    def threads(self):
        return self.main_window_ui.thread_count.value()

    def set_threads(self, threads):
        self.main_window_ui.thread_count.setValue(threads)

    @Slot(object)
    def update_progress_statistics(self, statistics: ProxyCheckerStatistics):
        self.main_window_ui.good_http.setText(str(statistics.good_http()))
        self.main_window_ui.good_socks4.setText(str(statistics.good_socks4()))
        self.main_window_ui.good_socks5.setText(str(statistics.good_socks5()))
        self.main_window_ui.total_bad_proxy.setText(str(statistics.bad_proxy()))
        self.main_window_ui.total_good_proxy.setText(str(statistics.good_proxy()))
        self.update_progress_bar(statistics)

    def update_progress_bar(self, statistics: ProxyCheckerStatistics):
        self.main_window_ui.progressBar.setMaximum(statistics.total())
        self.main_window_ui.progressBar.setValue(statistics.passed())
        self.main_window_ui.progressBar.setFormat('{}% ({} / {})'.format(
            str(statistics.progress_in_percent()),
            str(statistics.passed()),
            str(statistics.total())
        ))

    def __get_url(self):
        return self.main_window_ui.url_field.text()

    def __set_start_mode(self, value: bool):
        self.main_window_ui.start_btn.setEnabled(not value)
        self.main_window_ui.stop_btn.setEnabled(value)
        self.main_window_ui.import_http.setEnabled(not value)
        self.main_window_ui.import_socks4.setEnabled(not value)
        self.main_window_ui.import_socks5.setEnabled(not value)
        self.main_window_ui.clear_http.setEnabled(not value)
        self.main_window_ui.clear_socks4.setEnabled(not value)
        self.main_window_ui.clear_socks5.setEnabled(not value)
        self.main_window_ui.reset_button.setEnabled(not value)
        self.main_window_ui.timeout.setEnabled(not value)
        self.main_window_ui.thread_count.setEnabled(not value)
        self.main_window_ui.url_field.setEnabled(not value)

    @Slot()
    def reset(self):
        self.__proxy_checker = None
        self.__proxy_storage.clear()
        self.update_progress_statistics(ProxyCheckerStatistics())
        self.main_window_ui.progressBar.setFormat("0%")
        self.main_window_ui.progressBar.setValue(0)
        self.main_window_ui.progressBar.setMaximum(1)


