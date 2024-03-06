from PyQt5 import QtWidgets, QtGui, QtCore

class LibraryWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super(LibraryWidget, self).__init__(parent)

        self.setGeometry(QtCore.QRect(280, -30, 721, 761))
        self.setObjectName("LibraryWidget")
        
        self.rest = QtWidgets.QLabel(self)
        self.rest.setGeometry(QtCore.QRect(0, 0, 281, 761))
        self.rest.setText("Library ***************8")
        self.setObjectName("tryLabel")