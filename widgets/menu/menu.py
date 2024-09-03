from PyQt5 import QtWidgets, QtGui, QtCore
from .components import *
from constants import *

from res.colors import *

class Menu(QtWidgets.QWidget):

    def __init__(self, parent, pressFunc):
        super().__init__(parent)

        self.pressFunc = pressFunc

        self.setGeometry(QtCore.QRect(0, 0, 281, 761))
        self.setStyleSheet(f"background-color: {MENU_CLR};")
        self.setObjectName("Menu")

        self.rest = QtWidgets.QLabel(self)
        self.rest.setGeometry(QtCore.QRect(0, 0, 281, 761))
        self.rest.setStyleSheet(f"background-color: {MENU_CLR};")
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
        self.HomeSlot = MenuSlot(self, "home_icon.png", HOME_TXT)
        self.HomeSlot.clicked.connect(self.slotClicked)
        self.verticalLayout.addWidget(self.HomeSlot)

        # Reports slot
        self.ReportsSlot = MenuSlot(self, "report_icon.png", REPORTS_TXT)
        self.ReportsSlot.clicked.connect(self.slotClicked)
        self.verticalLayout.addWidget(self.ReportsSlot)

        # # Analytics Slot
        # self.AnalyticsSlot = MenuSlot(self, "analytics_icon.png", ANALYTICS_TXT)
        # self.AnalyticsSlot.clicked.connect(self.slotClicked)
        # self.verticalLayout.addWidget(self.AnalyticsSlot)

        # vertical spacer to push all up
        self.spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(self.spacerItem)

    def slotClicked(self, clicked_slot: MenuSlot):
        for slot in [self.HomeSlot, self.ReportsSlot]:
            if slot != clicked_slot:
                slot.onLeave()
        self.pressFunc(clicked_slot.label.text())

    