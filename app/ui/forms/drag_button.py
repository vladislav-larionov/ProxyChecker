from PySide2.QtCore import Signal, QObject
from PySide2.QtGui import QDropEvent
from PySide2.QtWidgets import QPushButton


class DragButtonSignals(QObject):
    file_dropped = Signal(set)


class DragButton(QPushButton):
    def __init__(self, parent, title=""):
        super(DragButton, self).__init__(title, parent)
        self.setAcceptDrops(True)
        self.signals = DragButtonSignals()

    def dragEnterEvent(self, e):
        if e.mimeData().hasFormat('application/x-qt-windows-mime;value="FileName"') \
                and e.mimeData().text().endswith('.txt'):
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e: QDropEvent):
        with open(e.mimeData().text().replace("file:///", ''), "r", encoding='utf8') as file:
            self.signals.file_dropped.emit(set(file.readlines()))

