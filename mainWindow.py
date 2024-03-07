from PyQt5 import QtCore, QtGui, QtWidgets
from widgets.menu.menu import Menu
from widgets.home.homeWidget import HomeWidget

from widgets.library.library import LibraryWidget
from constants import *


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # main window
        self.setObjectName("mainWindow")
        self.setWindowTitle("APPLYSIA")
        # TODO change window icon
        self.setFixedSize(1000, 750)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 125, 105))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 125, 105))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 125, 105))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.setPalette(palette)

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.menu = Menu(self.centralwidget, self.menuSlotClicked)

        self.actionWindow = HomeWidget(self.centralwidget)

        self.setCentralWidget(self.centralwidget)

    def menuSlotClicked(self, slotName):
        # check if clicked on open window slot
        if slotName in self.actionWindow.objectName():
            return
        self.actionWindow.hide()
        if slotName == HOME_TXT:
            self.actionWindow = HomeWidget(self.centralwidget)
        elif slotName == REPORTS_TXT:
            self.actionWindow = LibraryWidget(self.centralwidget)
        elif slotName == ANALYTICS_TXT:
            pass
        self.actionWindow.show()


    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    self = MainWindow()
    self.show()
    sys.exit(app.exec_())
