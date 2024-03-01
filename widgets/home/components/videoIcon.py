from PyQt5 import QtWidgets, QtGui, QtCore

class VideoIcon(QtWidgets.QLabel):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.setMaximumSize(QtCore.QSize(50, 50))
        self.setText("")
        self.setPixmap(QtGui.QPixmap("res/icons/video_icon.png"))
        self.setScaledContents(True)
        self.setObjectName("videoIcon")