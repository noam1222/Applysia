from PyQt5 import QtWidgets, QtGui, QtCore
from .components import *

class Menu(QtWidgets.QWidget):
    def __init__(self, parent):
        super(Menu, self).__init__(parent)

        self = QtWidgets.QWidget(parent)
        self.setGeometry(QtCore.QRect(0, 0, 281, 761))
        self.setStyleSheet("background-color: #FEF8F8;")
        self.setObjectName("Menu")

        # vertical layout for the menu
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")

        # APPLYSIA label
        self.headline = Headline(self, "APPLYSIA")
        self.verticalLayout.addWidget(self.headline)

        # Home slot
        self.HomeSlot = MenuSlot(self, "home_icon.png", "Home")
        self.verticalLayout.addWidget(self.HomeSlot)

        # Reports slot
        self.ReportsSlot = MenuSlot(self, "report_icon.png", "Reports")
        self.verticalLayout.addWidget(self.ReportsSlot)

        # Analytics Slot
        self.AnalyticsSlot = MenuSlot(self, "analytics_icon.png", "Analytics")
        self.verticalLayout.addWidget(self.AnalyticsSlot)

        # vertical spacer to push all up
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)