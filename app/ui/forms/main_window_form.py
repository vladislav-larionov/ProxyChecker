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
        MainWindow.resize(504, 323)
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
        self.layoutWidget1.setGeometry(QRect(20, 50, 271, 22))
        self.url_setting = QHBoxLayout(self.layoutWidget1)
        self.url_setting.setObjectName(u"url_setting")
        self.url_setting.setContentsMargins(0, 0, 0, 0)
        self.url_field = QLineEdit(self.layoutWidget1)
        self.url_field.setObjectName(u"url_field")

        self.url_setting.addWidget(self.url_field)

        self.url = QLabel(self.layoutWidget1)
        self.url.setObjectName(u"url")

        self.url_setting.addWidget(self.url)

        self.layoutWidget2 = QWidget(self.centralwidget)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(20, 100, 239, 25))
        self.managment = QHBoxLayout(self.layoutWidget2)
        self.managment.setObjectName(u"managment")
        self.managment.setContentsMargins(0, 0, 0, 0)
        self.reset_button = QPushButton(self.layoutWidget2)
        self.reset_button.setObjectName(u"reset_button")

        self.managment.addWidget(self.reset_button)

        self.stop_btn = QPushButton(self.layoutWidget2)
        self.stop_btn.setObjectName(u"stop_btn")
        self.stop_btn.setEnabled(False)

        self.managment.addWidget(self.stop_btn)

        self.start_btn = QPushButton(self.layoutWidget2)
        self.start_btn.setObjectName(u"start_btn")

        self.managment.addWidget(self.start_btn)

        self.layoutWidget4 = QWidget(self.centralwidget)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(270, 140, 151, 91))
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

        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 140, 191, 91))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.import_socks5 = DragButton(self.gridLayoutWidget)
        self.import_socks5.setObjectName(u"import_socks5")

        self.gridLayout.addWidget(self.import_socks5, 2, 2, 1, 1)

        self.import_socks4 = DragButton(self.gridLayoutWidget)
        self.import_socks4.setObjectName(u"import_socks4")

        self.gridLayout.addWidget(self.import_socks4, 1, 2, 1, 1)

        self.import_http = DragButton(self.gridLayoutWidget)
        self.import_http.setObjectName(u"import_http")

        self.gridLayout.addWidget(self.import_http, 0, 2, 1, 1)

        self.clear_http = QPushButton(self.gridLayoutWidget)
        self.clear_http.setObjectName(u"clear_http")

        self.gridLayout.addWidget(self.clear_http, 0, 1, 1, 1)

        self.clear_socks4 = QPushButton(self.gridLayoutWidget)
        self.clear_socks4.setObjectName(u"clear_socks4")

        self.gridLayout.addWidget(self.clear_socks4, 1, 1, 1, 1)

        self.clear_socks5 = QPushButton(self.gridLayoutWidget)
        self.clear_socks5.setObjectName(u"clear_socks5")

        self.gridLayout.addWidget(self.clear_socks5, 2, 1, 1, 1)

        self.http_count = QLabel(self.gridLayoutWidget)
        self.http_count.setObjectName(u"http_count")

        self.gridLayout.addWidget(self.http_count, 0, 0, 1, 1)

        self.socks5_count = QLabel(self.gridLayoutWidget)
        self.socks5_count.setObjectName(u"socks5_count")

        self.gridLayout.addWidget(self.socks5_count, 1, 0, 1, 1)

        self.socks4_count = QLabel(self.gridLayoutWidget)
        self.socks4_count.setObjectName(u"socks4_count")

        self.gridLayout.addWidget(self.socks4_count, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)
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
        self.reset_button.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.stop_btn.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.start_btn.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.good_socks5.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.good_socks4.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.good_http.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"http:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"socks4", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"socks4", None))
        self.import_socks5.setText(QCoreApplication.translate("MainWindow", u"SOCKS5", None))
        self.import_socks4.setText(QCoreApplication.translate("MainWindow", u"SOCKS4", None))
        self.import_http.setText(QCoreApplication.translate("MainWindow", u"HTTP", None))
        self.clear_http.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.clear_socks4.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.clear_socks5.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.http_count.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.socks5_count.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.socks4_count.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

