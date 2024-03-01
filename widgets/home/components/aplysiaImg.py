from PyQt5 import QtWidgets, QtGui, QtCore

class AplysiaImg(QtWidgets.QLabel):
    def __init__(self, parent):
        super().__init__(parent)

        self.setMaximumSize(QtCore.QSize(488, 302))
        self.setStyleSheet("")
        self.setText("")
        self.setPixmap(QtGui.QPixmap("res/imgs/aplysia.png"))
        self.setScaledContents(True)
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setWordWrap(False)
        self.setObjectName("aplysiaCartoon")