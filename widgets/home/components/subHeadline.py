from PyQt5 import QtWidgets, QtGui

class SubHeadline(QtWidgets.QLabel):
    def __init__(self, parent, text, name):
        super().__init__(parent)

        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.setFont(font)
        self.setText(text)
        self.setObjectName(name)
        

