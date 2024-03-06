from PyQt5 import QtWidgets, QtGui, QtCore
from .components import *

class Menu(QtWidgets.QWidget):

    def __init__(self, parent):
        super().__init__(parent)

        self.setGeometry(QtCore.QRect(0, 0, 281, 761))
        self.setStyleSheet("background-color: #FEF8F8;")
        self.setObjectName("Menu")

        self.rest = QtWidgets.QLabel(self)
        self.rest.setGeometry(QtCore.QRect(0, 0, 281, 761))
        self.rest.setStyleSheet("background-color: #FEF8F8;")
        self.setObjectName("restLabel")

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
        self.HomeSlot.clicked.connect(self.slotClicked)
        self.verticalLayout.addWidget(self.HomeSlot)

        # Reports slot
        self.ReportsSlot = MenuSlot(self, "report_icon.png", "Reports")
        self.ReportsSlot.clicked.connect(self.slotClicked)
        self.verticalLayout.addWidget(self.ReportsSlot)

        # Analytics Slot
        self.AnalyticsSlot = MenuSlot(self, "analytics_icon.png", "Analytics")
        self.AnalyticsSlot.clicked.connect(self.slotClicked)
        self.verticalLayout.addWidget(self.AnalyticsSlot)

        # vertical spacer to push all up
        self.spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(self.spacerItem)

    def slotClicked(self, clicked_slot):
        for slot in [self.HomeSlot, self.ReportsSlot, self.AnalyticsSlot]:
            if slot != clicked_slot:
                slot.onLeave()

    