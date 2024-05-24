from PyQt5 import QtWidgets, QtGui, QtCore
from constants import *
from widgets.home.components.toolBtn import ToolBtn

class LibraryWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super(LibraryWidget, self).__init__(parent)

        # set up
        self.setGeometry(QtCore.QRect(280, -30, 721, 761))
        self.setObjectName("LibraryWidget")
        
        # main Vertical Layout
        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 30, 721, 761))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(20, 0, 20, 10)
        self.verticalLayout.setObjectName("verticalLayout")

        # Headline
        self.libraryHeadline = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(45)
        self.libraryHeadline.setFont(font)
        self.libraryHeadline.setObjectName("libraryHeadline")
        self.verticalLayout.addWidget(self.libraryHeadline, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)

        # main Horizontal Layout: tree, tree, filters
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        # first tree: All, 1-5
        self.treeWidget = QtWidgets.QTreeWidget(self.verticalLayoutWidget)
        self.treeWidget.setStyleSheet("""
            background-color: #FFFDD0;  /* Cream color */
            border-top-left-radius: 10px;
            border-top-right-radius: 10px;
        """)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.treeWidget.setFont(font)
        self.treeWidget.setAllColumnsShowFocus(False)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setTextAlignment(0, QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.treeWidget.headerItem().setFont(0, font)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.treeWidget.header().setVisible(False)
        self.treeWidget.header().setCascadingSectionResizes(False)
        self.treeWidget.header().setDefaultSectionSize(100)
        self.horizontalLayout.addWidget(self.treeWidget)

        # tree 2: 6-12
        self.treeWidget_2 = QtWidgets.QTreeWidget(self.verticalLayoutWidget)
        self.treeWidget_2.setStyleSheet("""
            background-color: #FFFDD0;  /* Cream color */
            border-top-left-radius: 10px;
            border-top-right-radius: 10px;
        """)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.treeWidget_2.setFont(font)
        self.treeWidget_2.setAllColumnsShowFocus(False)
        self.treeWidget_2.setObjectName("treeWidget_2")
        self.treeWidget_2.headerItem().setTextAlignment(0, QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.treeWidget_2.headerItem().setFont(0, font)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
        self.treeWidget_2.header().setVisible(False)
        self.treeWidget_2.header().setCascadingSectionResizes(False)
        self.treeWidget_2.header().setDefaultSectionSize(100)
        self.horizontalLayout.addWidget(self.treeWidget_2)

        # filter Vertical layout
        #TODO fix decoration
        self.filterVerticalLayout = QtWidgets.QVBoxLayout()
        self.filterVerticalLayout.setSpacing(15)
        self.filterVerticalLayout.setObjectName("filterVerticalLayout")
        # filter headline
        self.filtersHeadlineLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Narkisim")
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.filtersHeadlineLabel.setFont(font)
        self.filtersHeadlineLabel.setObjectName("filtersHeadlineLabel")
        self.filterVerticalLayout.addWidget(self.filtersHeadlineLabel, 0, QtCore.Qt.AlignHCenter)
        
        #decoratin line
        self.line = QtWidgets.QFrame(self)
        self.line.setGeometry(QtCore.QRect(60, 80, 191, 16))
        self.line.setObjectName("line")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setStyleSheet("background-color: lightgray;")
        self.filterVerticalLayout.addWidget(self.line)

        #date filter
        self.dateFilter = QtWidgets.QHBoxLayout()
        self.dateFilter.setContentsMargins(-1, 0, -1, -1)
        self.dateFilter.setObjectName("dateFilter")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.dateFilter.addWidget(self.label_4)

        self.dateEditFilter = QtWidgets.QDateEdit(self.verticalLayoutWidget)
        self.dateEditFilter.setObjectName("dateEditFilter")
        current_date = QtCore.QDate.currentDate()
        self.dateEditFilter.setDate(current_date)
        self.dateEditFilter.setMaximumDate(current_date)
        self.dateFilter.addWidget(self.dateEditFilter)

        self.dateIconPicker = ToolBtn(self, "date_icon.png", "dateIconPicker", "Choose date", onClick=self.showCalendar)
        self.dateFilter.addWidget(self.dateIconPicker)

        self.filterVerticalLayout.addLayout(self.dateFilter)
        #time Filter
        self.timeFilterHL = QtWidgets.QHBoxLayout()
        self.timeFilterHL.setObjectName("timeFilterHL")
        self.timeLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.timeLabel.setFont(font)
        self.timeLabel.setObjectName("timeLabel")
        self.timeFilterHL.addWidget(self.timeLabel)
        self.timeEditFilterStart = QtWidgets.QTimeEdit(self.verticalLayoutWidget)
        self.timeEditFilterStart.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.timeEditFilterStart.setAccelerated(False)
        self.timeEditFilterStart.setObjectName("timeEditFilterStart")
        #TODO cahnge minutes to only get 00
        self.timeFilterHL.addWidget(self.timeEditFilterStart)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setStyleSheet("")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.timeFilterHL.addWidget(self.label_3)
        self.timeEditFilterEnd = QtWidgets.QTimeEdit(self.verticalLayoutWidget)
        self.timeEditFilterEnd.setCalendarPopup(False)
        self.timeEditFilterEnd.setObjectName("timeEditFilterEnd")
        #TODO cahnge minutes to only get 00
        self.timeFilterHL.addWidget(self.timeEditFilterEnd)
        self.filterVerticalLayout.addLayout(self.timeFilterHL)
        #movement filter
        self.MovementFilter = QtWidgets.QHBoxLayout()
        self.MovementFilter.setObjectName("MovementFilter")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.MovementFilter.addWidget(self.label_6)
        self.comboBoxLEQorBEQ = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBoxLEQorBEQ.setStyleSheet("background-color: #FFFDD0;  /* Cream color */")
        self.comboBoxLEQorBEQ.setObjectName("comboBoxLEQorBEQ")
        self.comboBoxLEQorBEQ.addItem("")
        self.comboBoxLEQorBEQ.addItem("")
        self.MovementFilter.addWidget(self.comboBoxLEQorBEQ)
        self.doubleSpinBoxMvmnt = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.doubleSpinBoxMvmnt.setMaximum(1.0)
        self.doubleSpinBoxMvmnt.setSingleStep(0.05)
        self.doubleSpinBoxMvmnt.setObjectName("doubleSpinBoxMvmnt")
        self.MovementFilter.addWidget(self.doubleSpinBoxMvmnt)
        self.filterVerticalLayout.addLayout(self.MovementFilter)
        #filter Button
        self.FilterBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.FilterBtn.setMinimumSize(QtCore.QSize(50, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.FilterBtn.setFont(font)
        self.FilterBtn.setStyleSheet("background-color:  #FFFDD0;  /* Cream color */"
"border-top-left-radius: 30px;\n"
"border-bottom-left-radius: 30px;\n"
"border-top-right-radius: 30px;\n"
"border-bottom-right-radius: 30px;\n"
"color: #dd4f4f;")
        self.FilterBtn.setObjectName("FilterBtn")
        self.filterVerticalLayout.addWidget(self.FilterBtn)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.filterVerticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.filterVerticalLayout)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, LibraryWindow):
        _translate = QtCore.QCoreApplication.translate
        LibraryWindow.setWindowTitle(_translate("LibraryWindow", "Form"))
        self.libraryHeadline.setText(_translate("LibraryWindow", "Reports Library"))
        self.treeWidget.headerItem().setText(0, _translate("LibraryWindow", "12.05.2024"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("LibraryWindow", "All"))
        self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("LibraryWindow", "06:00"))
        self.treeWidget.topLevelItem(0).child(1).setText(0, _translate("LibraryWindow", "07:00"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("LibraryWindow", "Aplysia 1"))
        self.treeWidget.topLevelItem(1).child(0).setText(0, _translate("LibraryWindow", "06:00"))
        self.treeWidget.topLevelItem(2).setText(0, _translate("LibraryWindow", "Aplysia 2"))
        self.treeWidget.topLevelItem(3).setText(0, _translate("LibraryWindow", "Aplysia 3"))
        self.treeWidget.topLevelItem(4).setText(0, _translate("LibraryWindow", "Aplysia 4"))
        self.treeWidget.topLevelItem(5).setText(0, _translate("LibraryWindow", "Aplysia 5"))
        self.treeWidget.topLevelItem(5).child(0).setText(0, _translate("LibraryWindow", "07:00"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.treeWidget_2.headerItem().setText(0, _translate("LibraryWindow", "12.05.2024"))
        __sortingEnabled = self.treeWidget_2.isSortingEnabled()
        self.treeWidget_2.setSortingEnabled(False)
        self.treeWidget_2.topLevelItem(0).setText(0, _translate("LibraryWindow", "Aplysia 6"))
        self.treeWidget_2.topLevelItem(1).setText(0, _translate("LibraryWindow", "Aplysia 7"))
        self.treeWidget_2.topLevelItem(1).child(0).setText(0, _translate("LibraryWindow", "07:00"))
        self.treeWidget_2.topLevelItem(2).setText(0, _translate("LibraryWindow", "Aplysia 8"))
        self.treeWidget_2.topLevelItem(3).setText(0, _translate("LibraryWindow", "Aplysia 9"))
        self.treeWidget_2.topLevelItem(4).setText(0, _translate("LibraryWindow", "Aplysia 10"))
        self.treeWidget_2.topLevelItem(4).child(0).setText(0, _translate("LibraryWindow", "06:00"))
        self.treeWidget_2.topLevelItem(4).child(1).setText(0, _translate("LibraryWindow", "07:00"))
        self.treeWidget_2.topLevelItem(5).setText(0, _translate("LibraryWindow", "Aplysia 11"))
        self.treeWidget_2.topLevelItem(6).setText(0, _translate("LibraryWindow", "Aplysia 12"))
        self.treeWidget_2.setSortingEnabled(__sortingEnabled)
        self.filtersHeadlineLabel.setText(_translate("LibraryWindow", "Filters"))
        self.label_4.setText(_translate("LibraryWindow", "Date: "))
        self.timeLabel.setText(_translate("LibraryWindow", "Time: "))
        self.label_3.setText(_translate("LibraryWindow", "-"))
        self.label_6.setText(_translate("LibraryWindow", "Movement "))
        self.comboBoxLEQorBEQ.setItemText(0, _translate("LibraryWindow", "More than"))
        self.comboBoxLEQorBEQ.setItemText(1, _translate("LibraryWindow", "Less than"))
        self.FilterBtn.setText(_translate("LibraryWindow", "Filter"))

    def showCalendar(self):
        self.calendarWidget = QtWidgets.QCalendarWidget(self.parent())
        self.calendarWidget.setGeometry(QtCore.QRect(350, 275, 391, 241))
        self.calendarWidget.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Israel))
        self.calendarWidget.setStyleSheet("background-color: lightblue;")
        self.calendarWidget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        
        # Disable future dates
        current_date = QtCore.QDate.currentDate()
        self.calendarWidget.setMaximumDate(current_date)
        future_date_format = QtGui.QTextCharFormat()
        future_date_format.setForeground(QtCore.Qt.gray)
        for offset in range(1, 32):
            future_date = current_date.addDays(offset)
            self.calendarWidget.setDateTextFormat(future_date, future_date_format)

        self.calendarWidget.setObjectName("calendarWidget")
        self.calendarWidget.activated.connect(self.dateChoosed)
        self.calendarWidget.show()

    def dateChoosed(self, date):
        self.dateEditFilter.setDate(date)
        self.calendarWidget.hide()