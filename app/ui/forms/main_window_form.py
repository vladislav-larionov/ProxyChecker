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

from ui.forms.drag_button import DragButton

from  . import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(450, 305)
        MainWindow.setCursor(QCursor(Qt.ArrowCursor))
        MainWindow.setMouseTracking(True)
        MainWindow.setLayoutDirection(Qt.RightToLeft)
        MainWindow.setAutoFillBackground(False)
        self.home_directory = QAction(MainWindow)
        self.home_directory.setObjectName(u"home_directory")
        icon = QIcon()
        icon.addFile(u":/resources/resources/Folder.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.home_directory.setIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget1 = QWidget(self.centralwidget)
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

        self.layoutWidget4 = QWidget(self.centralwidget)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(270, 150, 151, 91))
        self.statistic = QGridLayout(self.layoutWidget4)
        self.statistic.setObjectName(u"statistic")
        self.statistic.setContentsMargins(0, 0, 0, 0)
        self.good_socks5 = QLabel(self.layoutWidget4)
        self.good_socks5.setObjectName(u"good_socks5")

        self.statistic.addWidget(self.good_socks5, 2, 1, 1, 1)

        self.good_socks4 = QLabel(self.layoutWidget4)
        self.good_socks4.setObjectName(u"good_socks4")

        self.statistic.addWidget(self.good_socks4, 1, 1, 1, 1)

        self.good_http = QLabel(self.layoutWidget4)
        self.good_http.setObjectName(u"good_http")

        self.statistic.addWidget(self.good_http, 0, 1, 1, 1)

        self.label = QLabel(self.layoutWidget4)
        self.label.setObjectName(u"label")

        self.statistic.addWidget(self.label, 0, 2, 1, 1)

        self.label_2 = QLabel(self.layoutWidget4)
        self.label_2.setObjectName(u"label_2")

        self.statistic.addWidget(self.label_2, 1, 2, 1, 1)

        self.label_3 = QLabel(self.layoutWidget4)
        self.label_3.setObjectName(u"label_3")

        self.statistic.addWidget(self.label_3, 2, 2, 1, 1)

        self.import_socks5 = DragButton(self.centralwidget)
        self.import_socks5.setObjectName(u"import_socks5")
        self.import_socks5.setGeometry(QRect(20, 187, 91, 23))
        self.socks5_count = QLineEdit(self.centralwidget)
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
        self.clear_socks5 = QPushButton(self.centralwidget)
        self.clear_socks5.setObjectName(u"clear_socks5")
        self.clear_socks5.setGeometry(QRect(190, 189, 21, 23))
        self.import_socks4 = DragButton(self.centralwidget)
        self.import_socks4.setObjectName(u"import_socks4")
        self.import_socks4.setGeometry(QRect(20, 158, 91, 23))
        self.socks4_count = QLineEdit(self.centralwidget)
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
        self.clear_socks4 = QPushButton(self.centralwidget)
        self.clear_socks4.setObjectName(u"clear_socks4")
        self.clear_socks4.setGeometry(QRect(190, 160, 21, 23))
        self.clear_http = QPushButton(self.centralwidget)
        self.clear_http.setObjectName(u"clear_http")
        self.clear_http.setGeometry(QRect(190, 132, 21, 23))
        self.http_count = QLineEdit(self.centralwidget)
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
        self.import_http = DragButton(self.centralwidget)
        self.import_http.setObjectName(u"import_http")
        self.import_http.setGeometry(QRect(20, 130, 91, 23))
        self.total_proxy_count_label = QLabel(self.centralwidget)
        self.total_proxy_count_label.setObjectName(u"total_proxy_count_label")
        self.total_proxy_count_label.setGeometry(QRect(270, 60, 47, 13))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(270, 80, 47, 13))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(270, 100, 47, 13))
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setEnabled(False)
        self.progressBar.setGeometry(QRect(270, 120, 151, 23))
        self.progressBar.setLayoutDirection(Qt.LeftToRight)
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(15000)
        self.progressBar.setValue(0)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.layoutWidget100 = QWidget(self.centralwidget)
        self.layoutWidget100.setObjectName(u"layoutWidget100")
        self.layoutWidget100.setGeometry(QRect(20, 60, 191, 61))
        self.verticalLayout = QVBoxLayout(self.layoutWidget100)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.start_btn = QPushButton(self.layoutWidget100)
        self.start_btn.setObjectName(u"start_btn")

        self.verticalLayout.addWidget(self.start_btn)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.reset_button = QPushButton(self.layoutWidget100)
        self.reset_button.setObjectName(u"reset_button")

        self.horizontalLayout.addWidget(self.reset_button)

        self.stop_btn = QPushButton(self.layoutWidget100)
        self.stop_btn.setObjectName(u"stop_btn")
        self.stop_btn.setEnabled(False)

        self.horizontalLayout.addWidget(self.stop_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 220, 191, 22))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.timeout = QLineEdit(self.layoutWidget)
        self.timeout.setObjectName(u"timeout")
        self.timeout.setToolTipDuration(1)
        self.timeout.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.timeout)

        self.thread_count = QLineEdit(self.layoutWidget)
        self.thread_count.setObjectName(u"thread_count")
        self.thread_count.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.thread_count)

        self.total_proxy_loaded = QLabel(self.centralwidget)
        self.total_proxy_loaded.setObjectName(u"total_proxy_loaded")
        self.total_proxy_loaded.setGeometry(QRect(340, 60, 47, 13))
        self.total_proxy_loaded.setAlignment(Qt.AlignCenter)
        self.total_bad_proxy = QLabel(self.centralwidget)
        self.total_bad_proxy.setObjectName(u"total_bad_proxy")
        self.total_bad_proxy.setGeometry(QRect(340, 80, 47, 13))
        self.total_bad_proxy.setAlignment(Qt.AlignCenter)
        self.total_good_proxy = QLabel(self.centralwidget)
        self.total_good_proxy.setObjectName(u"total_good_proxy")
        self.total_good_proxy.setGeometry(QRect(340, 100, 47, 13))
        self.total_good_proxy.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setEnabled(True)
        self.toolBar.setAutoFillBackground(True)
        self.toolBar.setMovable(False)
        self.toolBar.setAllowedAreas(Qt.AllToolBarAreas)
        self.toolBar.setOrientation(Qt.Horizontal)
        self.toolBar.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolBar.setFloatable(True)
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.toolBar.addAction(self.home_directory)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ProxyChecker", None))
        self.home_directory.setText(QCoreApplication.translate("MainWindow", u"Home directory", None))
        self.url_field.setText(QCoreApplication.translate("MainWindow", u"https://mail.ru", None))
        self.url.setText(QCoreApplication.translate("MainWindow", u"URL:", None))
        self.good_socks5.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.good_socks4.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.good_http.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"HTTP:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"SOCKS4:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"SOCKS5:", None))
        self.import_socks5.setText(QCoreApplication.translate("MainWindow", u"SOCKS5", None))
        self.socks5_count.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.clear_socks5.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.import_socks4.setText(QCoreApplication.translate("MainWindow", u"SOCKS4", None))
        self.socks4_count.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.clear_socks4.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.clear_http.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.http_count.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.import_http.setText(QCoreApplication.translate("MainWindow", u"HTTP", None))
        self.total_proxy_count_label.setText(QCoreApplication.translate("MainWindow", u"Loaded:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Bad:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Good:", None))
        self.progressBar.setFormat(QCoreApplication.translate("MainWindow", u"%p%", None))
        self.start_btn.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.reset_button.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.stop_btn.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
#if QT_CONFIG(tooltip)
        self.timeout.setToolTip(QCoreApplication.translate("MainWindow", u"timeout", None))
#endif // QT_CONFIG(tooltip)
        self.timeout.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.timeout.setPlaceholderText("")
#if QT_CONFIG(tooltip)
        self.thread_count.setToolTip(QCoreApplication.translate("MainWindow", u"thread", None))
#endif // QT_CONFIG(tooltip)
        self.thread_count.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.total_proxy_loaded.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.total_bad_proxy.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.total_good_proxy.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

