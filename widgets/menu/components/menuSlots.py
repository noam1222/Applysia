from PyQt5 import QtWidgets, QtGui, QtCore
from constants import getIconPath

class MenuSlot(QtWidgets.QFrame):
    clicked = QtCore.pyqtSignal(object)
    def __init__(self, parent, icon, label_text):
        super().__init__(parent)
        
        self.setStyleSheet("QFrame{border-bottom: 1px solid rgba(0, 0, 0, 50%);}\n"
                           "QFrame:hover{background-color : rgb(156, 156, 156)}\n"
                           "QLabel{background-color: transparent;}")
        self.setObjectName("MenuSlot")

        # Horizontal layout for the icon and label
        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(8, 1, -1, -1)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # Icon
        self.icon = QtWidgets.QLabel(self)
        self.icon.setMaximumSize(QtCore.QSize(50, 50))
        self.icon.setStyleSheet("border-bottom: 0px;")
        self.icon.setPixmap(QtGui.QPixmap(getIconPath(icon)))
        self.icon.setObjectName("MenuIcon")
        self.horizontalLayout.addWidget(self.icon)

        # Label
        self.label = QtWidgets.QLabel(self)
        font = QtGui.QFont("Impact", 30, 50, False)
        self.label.setFont(font)
        self.label.setStyleSheet("border-bottom: 0px;")
        self.label.setObjectName("MenuLabel")
        self.label.setText(label_text)
        self.horizontalLayout.addWidget(self.label)



    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.clicked.emit(self)
            self.setStyleSheet("QFrame{border-bottom: 1px solid rgba(0, 0, 0, 50%);background-color : rgb(120, 120, 120);}\n"
                           "QFrame:hover{background-color : rgb(156, 156, 156)}\n"
                           "QLabel{background-color: transparent;}")
        
    
    def onLeave(self):
        self.setStyleSheet("QFrame{border-bottom: 1px solid rgba(0, 0, 0, 50%);}\n"
                           "QFrame:hover{background-color : rgb(156, 156, 156)}\n"
                           "QLabel{background-color: transparent;}")
