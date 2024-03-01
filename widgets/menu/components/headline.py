from PyQt5 import QtWidgets, QtGui, QtCore


class Headline(QtWidgets.QLabel):
    def __init__(self, parent, text):
        super().__init__(parent)

        self.setText(text)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(188, 67, 67))
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        self.setPalette(palette)
        font = QtGui.QFont("Impact", 28, 50, False)
        self.setFont(font)
        self.setStyleSheet(
            "border-bottom: 1px solid rgba(0, 0, 0, 50%);")
        self.setFrameShadow(QtWidgets.QFrame.Plain)
        self.setTextFormat(QtCore.Qt.AutoText)
        self.setAlignment(
            QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.setObjectName("HeadlineLabel")
