from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QTreeWidget


class CustomTreeWidget(QTreeWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setDragEnabled(True)
        self.setAcceptDrops(False)

    def startDrag(self, actions):
        drag = QtGui.QDrag(self)
        mime_data = self.mimeData(self.selectedItems())
        drag.setMimeData(mime_data)
        drag.exec_(QtCore.Qt.MoveAction)

    def dragEnterEvent(self, event):
        event.ignore()

    def dragMoveEvent(self, event):
        event.ignore()

    def dropEvent(self, event):
        event.ignore()
