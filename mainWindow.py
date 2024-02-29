from PyQt5 import QtCore, QtGui, QtWidgets
from menuSlots import MenuSlot


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # main window
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("APPLYSIA")
        MainWindow.setFixedSize(974, 757)
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
        MainWindow.setPalette(palette)

        # menu widget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Menu = QtWidgets.QWidget(self.centralwidget)
        self.Menu.setGeometry(QtCore.QRect(0, 0, 251, 761))
        self.Menu.setStyleSheet("background-color: #FEF8F8;")
        self.Menu.setObjectName("Menu")

        # vertical layout in the menu
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Menu)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")

        # APPLYSIA label
        self.APPLYSIA_LABEL = QtWidgets.QLabel(self.Menu)
        self.APPLYSIA_LABEL.setText("APPLYSIA")
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.APPLYSIA_LABEL.sizePolicy().hasHeightForWidth())
        self.APPLYSIA_LABEL.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(188, 67, 67))
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        self.APPLYSIA_LABEL.setPalette(palette)
        font = QtGui.QFont("Impact", 28, 50, False)
        self.APPLYSIA_LABEL.setFont(font)
        self.APPLYSIA_LABEL.setStyleSheet(
            "border-bottom: 1px solid rgba(0, 0, 0, 50%);")
        self.APPLYSIA_LABEL.setFrameShadow(QtWidgets.QFrame.Plain)
        self.APPLYSIA_LABEL.setTextFormat(QtCore.Qt.AutoText)
        self.APPLYSIA_LABEL.setAlignment(
            QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.APPLYSIA_LABEL.setObjectName("APPLYSIA_LABEL")
        self.verticalLayout.addWidget(self.APPLYSIA_LABEL)

        # Home slot (in menu)
        self.HomeSlot = MenuSlot(self.Menu, "icons/home_icon.png", "Home")
        self.verticalLayout.addWidget(self.HomeSlot)

        # Reports slot (in menu)
        self.ReportsSlot = MenuSlot(self.Menu, "icons/report_icon.png", "Reports")
        self.verticalLayout.addWidget(self.ReportsSlot)

        # Analytics Slot
        self.AnalyticsSlot = MenuSlot(self.Menu, "icons/analytics_icon.png", "Analytics", font_size=26)
        self.verticalLayout.addWidget(self.AnalyticsSlot)

        # vertical spacer
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        MainWindow.setCentralWidget(self.centralwidget)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
