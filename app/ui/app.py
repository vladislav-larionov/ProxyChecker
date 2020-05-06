# pylint: disable=R0902
"""
Main window of the app
"""
import os

from PySide2.QtCore import Slot, SIGNAL
from PySide2.QtWidgets import QMainWindow, QFileDialog

from lib.proxy_checker import ProxyChecker
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
        self.connect(main_window_ui.clear_http, SIGNAL("clicked()"), self.clear_http)
        self.connect(main_window_ui.clear_socks4, SIGNAL("clicked()"), self.clear_socks4)
        self.connect(main_window_ui.clear_socks5, SIGNAL("clicked()"), self.clear_socks5)
        self.connect(main_window_ui.start_btn, SIGNAL("clicked()"), self.start_check)
        self.connect(main_window_ui.stop_btn, SIGNAL("clicked()"), self.stop_check)
        self.connect(main_window_ui.reset_button, SIGNAL("clicked()"), self.reset)
        self.connect(main_window_ui.home_directory, SIGNAL("triggered()"), self.open_home_directory)
        self.main_window_ui.import_http.signals.file_dropped.connect(self.import_http_form_drag_and_drop)
        self.main_window_ui.import_socks4.signals.file_dropped.connect(self.import_socks4_form_drag_and_drop)
        self.main_window_ui.import_socks5.signals.file_dropped.connect(self.import_socks5_form_drag_and_drop)

    @Slot()
    def open_home_directory(self):
        os.startfile(os.getcwd())

    def __init__(self):
        """ Constructor of widget """
        main_window = QMainWindow()
        self.main_window_ui = Ui_MainWindow()
        self.main_window_ui.setupUi(main_window)
        QMainWindow.__init__(self)
        Ui_MainWindow.setupUi(self.main_window_ui, self)
        self.signals(self.main_window_ui)
        self.imported_http = set()
        self.imported_socks4 = set()
        self.imported_socks5 = set()
        self.__proxy_checker = None

    @Slot()
    def import_http_form_file(self):
        self.__import_proxy_form_file(self.imported_http)

    @Slot()
    def import_socks4_form_file(self):
        self.__import_proxy_form_file(self.imported_socks4)

    @Slot()
    def import_socks5_form_file(self):
        self.__import_proxy_form_file(self.imported_socks5)

    def __import_proxy_form_file(self, proxy_list: set):
        file_name = QFileDialog.getOpenFileName(self, dir=self.tr("./"), filter=self.tr("*.txt"))
        if not file_name[0]:
            return
        with open(file_name[0], "r", encoding='utf8') as file:
            self.__import_proxy(proxy_list, file.readlines())
        self.update_imported_count()
        return proxy_list

    @Slot(set)
    def import_http_form_drag_and_drop(self, imported_proxy):
        self.__import_proxy(self.imported_http, imported_proxy)

    @Slot(set)
    def import_socks4_form_drag_and_drop(self, imported_proxy):
        self.__import_proxy(self.imported_socks4, imported_proxy)

    @Slot(set)
    def import_socks5_form_drag_and_drop(self, imported_proxy):
        self.__import_proxy(self.imported_socks5, imported_proxy)

    def __import_proxy(self, proxy_list: set, imported_proxy):
        proxy_list.update(set(map(lambda proxy: proxy.strip(), imported_proxy)))
        self.update_imported_count()
        return proxy_list

    @Slot()
    def clear_http(self):
        self.imported_http.clear()
        self.update_imported_count()

    @Slot()
    def clear_socks4(self):
        self.imported_socks4.clear()
        self.update_imported_count()

    @Slot()
    def clear_socks5(self):
        self.imported_socks5.clear()
        self.update_imported_count()

    def update_imported_count(self):
        self.main_window_ui.http_count.setText(str(len(self.imported_http)))
        self.main_window_ui.socks4_count.setText(str(len(self.imported_socks4)))
        self.main_window_ui.socks5_count.setText(str(len(self.imported_socks5)))

    @Slot()
    def start_check(self):
        self.__set_start_mode(True)
        self.__proxy_checker = ProxyChecker(
            url=self.__get_url(),
            socks4_proxies=self.imported_socks4,
            socks5_proxies=self.imported_socks5,
            http_proxies=self.imported_http
        )
        self.__proxy_checker.signals.valid_proxy_signal.connect(self.update_statistics)
        self.__proxy_checker.signals.done_signal.connect(self.set_stop_mode)
        self.__proxy_checker.start()

    @Slot(int, int, int)
    def update_statistics(self, http_count, socks4_count, socks5_count):
        self.main_window_ui.good_http.setText(str(http_count))
        self.main_window_ui.good_socks4.setText(str(socks4_count))
        self.main_window_ui.good_socks5.setText(str(socks5_count))

    @Slot()
    def stop_check(self):
        self.__proxy_checker.terminate()
        self.__proxy_checker.wait()
        self.__set_start_mode(False)

    def __get_url(self):
        return self.main_window_ui.url_field.text()

    @Slot()
    def set_stop_mode(self):
        self.__set_start_mode(False)

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

    @Slot()
    def reset(self):
        self.imported_socks5.clear()
        self.imported_socks4.clear()
        self.imported_http.clear()
        self.update_statistics(0, 0, 0)
        self.update_imported_count()


