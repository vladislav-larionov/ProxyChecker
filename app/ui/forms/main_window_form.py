# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window_form.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from .drag_button import DragButton
from .components.statistics_widget import StatisticsWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(450, 300)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(450, 300))
        MainWindow.setMaximumSize(QSize(450, 300))
        MainWindow.setCursor(QCursor(Qt.ArrowCursor))
        MainWindow.setMouseTracking(True)
        MainWindow.setLayoutDirection(Qt.RightToLeft)
        MainWindow.setAutoFillBackground(False)
        self.home_directory = QAction(MainWindow)
        self.home_directory.setObjectName(u"home_directory")
        self.home_directory.setIconVisibleInMenu(False)
        self.main_widget = QWidget(MainWindow)
        self.main_widget.setObjectName(u"main_widget")
        self.layoutWidget1 = QWidget(self.main_widget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 20, 271, 22))
        self.url_setting = QHBoxLayout(self.layoutWidget1)
        self.url_setting.setObjectName(u"url_setting")
        self.url_setting.setContentsMargins(0, 0, 0, 0)
        self.url_field = QLineEdit(self.layoutWidget1)
        self.url_field.setObjectName(u"url_field")

        self.url_setting.addWidget(self.url_field)

        self.url = QLabel(self.layoutWidget1)
        self.url.setObjectName(u"url")

        self.url_setting.addWidget(self.url)

        self.import_socks5 = DragButton(self.main_widget)
        self.import_socks5.setObjectName(u"import_socks5")
        self.import_socks5.setGeometry(QRect(20, 187, 91, 23))
        self.socks5_count = QLineEdit(self.main_widget)
        self.socks5_count.setObjectName(u"socks5_count")
        self.socks5_count.setEnabled(False)
        self.socks5_count.setGeometry(QRect(120, 190, 61, 20))
        self.socks5_count.setCursor(QCursor(Qt.ArrowCursor))
        self.socks5_count.setMouseTracking(False)
        self.socks5_count.setFocusPolicy(Qt.NoFocus)
        self.socks5_count.setContextMenuPolicy(Qt.NoContextMenu)
        self.socks5_count.setAcceptDrops(False)
        self.socks5_count.setStyleSheet(u":disabled { color:rgb(0, 0, 0); }")
        self.socks5_count.setFrame(True)
        self.socks5_count.setAlignment(Qt.AlignCenter)
        self.socks5_count.setReadOnly(True)
        self.clear_socks5 = QPushButton(self.main_widget)
        self.clear_socks5.setObjectName(u"clear_socks5")
        self.clear_socks5.setGeometry(QRect(190, 189, 21, 23))
        self.import_socks4 = DragButton(self.main_widget)
        self.import_socks4.setObjectName(u"import_socks4")
        self.import_socks4.setGeometry(QRect(20, 158, 91, 23))
        self.socks4_count = QLineEdit(self.main_widget)
        self.socks4_count.setObjectName(u"socks4_count")
        self.socks4_count.setEnabled(False)
        self.socks4_count.setGeometry(QRect(120, 161, 61, 20))
        self.socks4_count.setCursor(QCursor(Qt.ArrowCursor))
        self.socks4_count.setMouseTracking(False)
        self.socks4_count.setFocusPolicy(Qt.NoFocus)
        self.socks4_count.setContextMenuPolicy(Qt.NoContextMenu)
        self.socks4_count.setAcceptDrops(False)
        self.socks4_count.setStyleSheet(u":disabled { color:rgb(0, 0, 0); }")
        self.socks4_count.setFrame(True)
        self.socks4_count.setAlignment(Qt.AlignCenter)
        self.socks4_count.setReadOnly(True)
        self.clear_socks4 = QPushButton(self.main_widget)
        self.clear_socks4.setObjectName(u"clear_socks4")
        self.clear_socks4.setGeometry(QRect(190, 160, 21, 23))
        self.clear_http = QPushButton(self.main_widget)
        self.clear_http.setObjectName(u"clear_http")
        self.clear_http.setGeometry(QRect(190, 132, 21, 23))
        self.http_count = QLineEdit(self.main_widget)
        self.http_count.setObjectName(u"http_count")
        self.http_count.setEnabled(False)
        self.http_count.setGeometry(QRect(120, 133, 61, 20))
        self.http_count.setCursor(QCursor(Qt.ArrowCursor))
        self.http_count.setMouseTracking(False)
        self.http_count.setFocusPolicy(Qt.NoFocus)
        self.http_count.setContextMenuPolicy(Qt.NoContextMenu)
        self.http_count.setAcceptDrops(False)
        self.http_count.setStyleSheet(u":disabled { color:rgb(0, 0, 0); }")
        self.http_count.setFrame(True)
        self.http_count.setAlignment(Qt.AlignCenter)
        self.http_count.setReadOnly(True)
        self.import_http = DragButton(self.main_widget)
        self.import_http.setObjectName(u"import_http")
        self.import_http.setGeometry(QRect(20, 130, 91, 23))
        self.layoutWidget = QWidget(self.main_widget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 60, 191, 61))
        self.control_pane = QVBoxLayout(self.layoutWidget)
        self.control_pane.setObjectName(u"control_pane")
        self.control_pane.setContentsMargins(0, 0, 0, 0)
        self.start_btn = QPushButton(self.layoutWidget)
        self.start_btn.setObjectName(u"start_btn")

        self.control_pane.addWidget(self.start_btn)

        self.contol_layout = QHBoxLayout()
        self.contol_layout.setObjectName(u"contol_layout")
        self.reset_button = QPushButton(self.layoutWidget)
        self.reset_button.setObjectName(u"reset_button")

        self.contol_layout.addWidget(self.reset_button)

        self.stop_btn = QPushButton(self.layoutWidget)
        self.stop_btn.setObjectName(u"stop_btn")
        self.stop_btn.setEnabled(False)

        self.contol_layout.addWidget(self.stop_btn)


        self.control_pane.addLayout(self.contol_layout)

        self.layoutWidget2 = QWidget(self.main_widget)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(20, 220, 191, 22))
        self.settings_layout = QHBoxLayout(self.layoutWidget2)
        self.settings_layout.setObjectName(u"settings_layout")
        self.settings_layout.setContentsMargins(0, 0, 0, 0)
        self.timeout = QDoubleSpinBox(self.layoutWidget2)
        self.timeout.setObjectName(u"timeout")
        self.timeout.setLayoutDirection(Qt.LeftToRight)
        self.timeout.setFrame(True)
        self.timeout.setAlignment(Qt.AlignCenter)
        self.timeout.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.timeout.setAccelerated(False)
        self.timeout.setKeyboardTracking(True)
        self.timeout.setProperty("showGroupSeparator", False)
        self.timeout.setDecimals(0)
        self.timeout.setMinimum(1.000000000000000)
        self.timeout.setMaximum(100.000000000000000)
        self.timeout.setValue(5.000000000000000)

        self.settings_layout.addWidget(self.timeout)

        self.thread_count = QDoubleSpinBox(self.layoutWidget2)
        self.thread_count.setObjectName(u"thread_count")
        self.thread_count.setLayoutDirection(Qt.LeftToRight)
        self.thread_count.setFrame(True)
        self.thread_count.setAlignment(Qt.AlignCenter)
        self.thread_count.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.thread_count.setAccelerated(False)
        self.thread_count.setKeyboardTracking(True)
        self.thread_count.setProperty("showGroupSeparator", False)
        self.thread_count.setDecimals(0)
        self.thread_count.setMinimum(1.000000000000000)
        self.thread_count.setMaximum(250.000000000000000)
        self.thread_count.setValue(100.000000000000000)

        self.settings_layout.addWidget(self.thread_count)

        self.statistics_widget = StatisticsWidget(self.main_widget)
        self.statistics_widget.setObjectName(u"statistics_widget")
        self.statistics_widget.setGeometry(QRect(250, 50, 181, 201))
        self.gridLayout = QGridLayout(self.statistics_widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.good_http = QLabel(self.statistics_widget)
        self.good_http.setObjectName(u"good_http")
        self.good_http.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.good_http, 3, 1, 1, 1)

        self.total_good_proxy = QLabel(self.statistics_widget)
        self.total_good_proxy.setObjectName(u"total_good_proxy")
        self.total_good_proxy.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.total_good_proxy, 2, 1, 1, 1)

        self.total_bad_proxy = QLabel(self.statistics_widget)
        self.total_bad_proxy.setObjectName(u"total_bad_proxy")
        self.total_bad_proxy.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.total_bad_proxy, 1, 1, 1, 1)

        self.total_proxy_loaded = QLabel(self.statistics_widget)
        self.total_proxy_loaded.setObjectName(u"total_proxy_loaded")
        self.total_proxy_loaded.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.total_proxy_loaded, 0, 1, 1, 1)

        self.progressBar = QProgressBar(self.statistics_widget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setEnabled(False)
        self.progressBar.setLayoutDirection(Qt.LeftToRight)
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(15000)
        self.progressBar.setValue(0)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)

        self.gridLayout.addWidget(self.progressBar, 6, 1, 1, 2)

        self.good_count_label = QLabel(self.statistics_widget)
        self.good_count_label.setObjectName(u"good_count_label")

        self.gridLayout.addWidget(self.good_count_label, 2, 2, 1, 1)

        self.total_proxy_count_label = QLabel(self.statistics_widget)
        self.total_proxy_count_label.setObjectName(u"total_proxy_count_label")

        self.gridLayout.addWidget(self.total_proxy_count_label, 0, 2, 1, 1)

        self.bad_count_label = QLabel(self.statistics_widget)
        self.bad_count_label.setObjectName(u"bad_count_label")

        self.gridLayout.addWidget(self.bad_count_label, 1, 2, 1, 1)

        self.good_socks4 = QLabel(self.statistics_widget)
        self.good_socks4.setObjectName(u"good_socks4")
        self.good_socks4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.good_socks4, 4, 1, 1, 1)

        self.socks4_label = QLabel(self.statistics_widget)
        self.socks4_label.setObjectName(u"socks4_label")

        self.gridLayout.addWidget(self.socks4_label, 4, 2, 1, 1)

        self.http_label = QLabel(self.statistics_widget)
        self.http_label.setObjectName(u"http_label")

        self.gridLayout.addWidget(self.http_label, 3, 2, 1, 1)

        self.good_socks5 = QLabel(self.statistics_widget)
        self.good_socks5.setObjectName(u"good_socks5")
        self.good_socks5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.good_socks5, 5, 1, 1, 1)

        self.socks5_label = QLabel(self.statistics_widget)
        self.socks5_label.setObjectName(u"socks5_label")

        self.gridLayout.addWidget(self.socks5_label, 5, 2, 1, 1)

        MainWindow.setCentralWidget(self.main_widget)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setEnabled(True)
        self.toolBar.setLayoutDirection(Qt.LeftToRight)
        self.toolBar.setAutoFillBackground(True)
        self.toolBar.setMovable(False)
        self.toolBar.setAllowedAreas(Qt.AllToolBarAreas)
        self.toolBar.setOrientation(Qt.Horizontal)
        self.toolBar.setToolButtonStyle(Qt.ToolButtonTextOnly)
        self.toolBar.setFloatable(True)
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.toolBar.addAction(self.home_directory)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ProxyChecker", None))
        self.home_directory.setText(QCoreApplication.translate("MainWindow", u"Home directory", None))
        self.home_directory.setIconText(QCoreApplication.translate("MainWindow", u"Home directory", None))
        self.url_field.setText(QCoreApplication.translate("MainWindow", u"https://mail.ru", None))
        self.url.setText(QCoreApplication.translate("MainWindow", u"URL:", None))
        self.import_socks5.setText(QCoreApplication.translate("MainWindow", u"SOCKS5", None))
        self.socks5_count.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.clear_socks5.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.import_socks4.setText(QCoreApplication.translate("MainWindow", u"SOCKS4", None))
        self.socks4_count.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.clear_socks4.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.clear_http.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.http_count.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.import_http.setText(QCoreApplication.translate("MainWindow", u"HTTP", None))
        self.start_btn.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.reset_button.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.stop_btn.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.good_http.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.total_good_proxy.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.total_bad_proxy.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.total_proxy_loaded.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.progressBar.setFormat(QCoreApplication.translate("MainWindow", u"%p%", None))
        self.good_count_label.setText(QCoreApplication.translate("MainWindow", u"Good:", None))
        self.total_proxy_count_label.setText(QCoreApplication.translate("MainWindow", u"Loaded:", None))
        self.bad_count_label.setText(QCoreApplication.translate("MainWindow", u"Bad:", None))
        self.good_socks4.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.socks4_label.setText(QCoreApplication.translate("MainWindow", u"SOCKS4:", None))
        self.http_label.setText(QCoreApplication.translate("MainWindow", u"HTTP:", None))
        self.good_socks5.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.socks5_label.setText(QCoreApplication.translate("MainWindow", u"SOCKS5:", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

