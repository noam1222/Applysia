from PyQt5 import QtWidgets, QtGui, QtCore

class HeadlineHome(QtWidgets.QLabel):
    def __init__(self, parent, text):
        super().__init__(parent)
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(45)
        font.setKerning(True)
        self.setFont(font)
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setObjectName("homeHeadline")
        self.setText(text)