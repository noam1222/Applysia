from PyQt5 import QtWidgets, QtGui, QtCore
from constants import getIconPath

class ToolBtn(QtWidgets.QToolButton):
    def __init__(self, parent, icon, name):
        super().__init__(parent)

        self.setStyleSheet("background-color: transparent;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(getIconPath(icon)),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setIcon(icon1)
        self.setIconSize(QtCore.QSize(50, 50))
        self.setObjectName(name)