from PyQt5 import QtWidgets, QtGui, QtCore
from datetime import datetime

from .components import *
from constants import *
from widgets.report.report import Ui_ReportWidget
from db.controller import *
class HomeWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super(HomeWidget, self).__init__(parent)

        self.filePath = None

        self.setGeometry(QtCore.QRect(280, -30, 721, 761))
        self.setObjectName("HomeWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(
            self)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)

        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(30, -1, 30, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.headline = HeadlineHome(self, text="Home")
        self.verticalLayout_2.addWidget(self.headline)

        self.aplysiaCartoon = QtWidgets.QLabel()
        self.aplysiaCartoon.setMaximumSize(QtCore.QSize(488, 302))
        self.aplysiaCartoon.setStyleSheet("")
        self.aplysiaCartoon.setText("")
        self.aplysiaCartoon.setPixmap(QtGui.QPixmap(getImgPath("aplysia.png")))
        self.aplysiaCartoon.setScaledContents(True)
        self.aplysiaCartoon.setAlignment(QtCore.Qt.AlignCenter)
        self.aplysiaCartoon.setWordWrap(False)
        self.aplysiaCartoon.setObjectName("aplysiaCartoon")
        self.verticalLayout_2.addWidget(self.aplysiaCartoon)

        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)

        self.videoIcon = QtWidgets.QLabel()
        self.videoIcon.setMaximumSize(QtCore.QSize(50, 50))
        self.videoIcon.setText("")
        self.videoIcon.setPixmap(QtGui.QPixmap(getIconPath("video_icon.png")))
        self.videoIcon.setScaledContents(True)
        self.videoIcon.setObjectName("videoIcon")
        self.horizontalLayout_5.addWidget(self.videoIcon)

        self.chooseVideoBtn = QtWidgets.QPushButton(
            self)
        self.chooseVideoBtn.setEnabled(True)
        self.chooseVideoBtn.setBaseSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Ebrima")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.chooseVideoBtn.setFont(font)
        self.chooseVideoBtn.setText("Choose Video")
        self.chooseVideoBtn.setStyleSheet("background-color: black;\n"
                                          "color: white;\n"
                                          "border-radius: 5px;\n"
                                          "padding: 5px;")
        self.chooseVideoBtn.clicked.connect(self.openFileDialog)
        self.chooseVideoBtn.setObjectName("chooseVideoBtn")
        self.horizontalLayout_5.addWidget(self.chooseVideoBtn)

        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)

        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem4 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)

        self.dateLabel = SubHeadline(self, "Date:", "dateLabel")
        self.horizontalLayout_6.addWidget(self.dateLabel)

        self.dateTextEdit = TextEdit(self, "DD/MM/YY", "dateTextEdit")
        self.horizontalLayout_6.addWidget(self.dateTextEdit)

        self.dateToolBtn = ToolBtn(self, "date_icon.png", "dateToolBtn", "Choose date", onClick=self.showCalendar)
        self.horizontalLayout_6.addWidget(self.dateToolBtn)

        spacerItem5 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)

        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem6 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem6)

        self.timeLabel = SubHeadline(self, "Time:", "timeLabel")
        self.horizontalLayout_7.addWidget(self.timeLabel)

        self.timeEditText = TextEdit(self, "HH:MM", "timeEditText", readOnly=False)
        # Regular expression for time format HH:MM
        reg_exp = QtCore.QRegExp("^([01][0-9]|2[0-3]):[0-5][0-9]$")
        validator = QtGui.QRegExpValidator(reg_exp, self)
        self.timeEditText.setValidator(validator)
        self.timeEditText.textChanged.connect(self.timeChanged)
        # self.timeEditText.focusOutEvent = self.timeTextEditFocusOut
        self.horizontalLayout_7.addWidget(self.timeEditText)

        self.timeToolBtn = ToolBtn(self, "time_icon.png", "timeToolBtn", "Current time", onClick=self.setCurrentTime)
        self.horizontalLayout_7.addWidget(self.timeToolBtn)

        spacerItem7 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem7)

        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")

        spacerItem8 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem8)

        self.videoSpeedLabel = SubHeadline(self, "Speed of Video:", "videoSpeedLabel")
        self.horizontalLayout_9.addWidget(self.videoSpeedLabel)

        self.videoSpeedComboBox = QtWidgets.QComboBox(
            self)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(13)
        font.setKerning(True)
        self.videoSpeedComboBox.setFont(font)
        self.videoSpeedComboBox.setStyleSheet("border-radius: 10px;\n"
                                              "background: white;\n"
                                              "border: 1px solid gray;\n"
                                              "padding: 4px 4px 4px 4px;")
        self.videoSpeedComboBox.setObjectName("videoSpeedComboBox")
        self.videoSpeedComboBox.addItem("1.0")
        self.videoSpeedComboBox.addItem("1.25")
        self.videoSpeedComboBox.addItem("1.5")
        self.videoSpeedComboBox.addItem("1.75")
        self.videoSpeedComboBox.addItem("2.0")
        self.horizontalLayout_9.addWidget(self.videoSpeedComboBox)

        spacerItem9 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem9)

        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.analyzeBtn = QtWidgets.QPushButton(self)
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.analyzeBtn.setFont(font)
        self.analyzeBtn.setText("Analyze")
        self.analyzeBtn.setStyleSheet("background-color: rgb(255, 255, 178);\n"
                                      "color: black;\n"
                                      "border-radius: 5px;\n"
                                      "padding: 5px;")
        self.analyzeBtn.setObjectName("analyzeBtn")
        self.analyzeBtn.clicked.connect(self.analyzeBtnClicked)
        self.verticalLayout_2.addWidget(self.analyzeBtn)
        
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        spacerItem10 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem10)

    def openFileDialog(self):
        options = QtWidgets.QFileDialog.Options()
        filePath, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Choose Video", "", "Video Files (*.mp4 *.avi *.mov)", options=options)
        if not filePath:
            return
        self.filePath = filePath
        videoName = filePath.split('/')[-1]
        self.chooseVideoBtn.setText(videoName)

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
        self.dateTextEdit.setText(date.toString("dd/MM/yy"))
        self.calendarWidget.hide()

    def setCurrentTime(self):
        current_time = datetime.now().strftime("%H:%M")
        self.timeEditText.setText(current_time[0:3] + "00")

    def timeChanged(self):
        time = self.timeEditText.text()
        if len(time) >= 2:
            self.timeEditText.blockSignals(True)
            self.timeEditText.setText(time[:2] + ":00")
            self.timeEditText.blockSignals(False)

    def analyzeBtnClicked(self):
        # # check for correct date input
        # if self.dateTextEdit.text() == "":
        #     QtWidgets.QMessageBox.warning(self, "Invalid Date", "Please enter a valid date (use the calendar icon)")
        #     return
        # # check for correct time input
        # if not self.timeEditText.validator().regExp().exactMatch(self.timeEditText.text()):
        #     QtWidgets.QMessageBox.warning(self, "Invalid Time", "Please enter a valid time in the format HH:MM.")
        #     return
        # # check if user choose video
        # if not self.filePath:
        #     QtWidgets.QMessageBox.warning(self, "Invalid Video", "Please Choose video.")
        #     return
        
        # get the report from DB
        reports = get_report_by_date_and_time(self.dateTextEdit.text(), self.timeEditText.text())

        # open the report
        self.ReportWidget = QtWidgets.QWidget()
        ui = Ui_ReportWidget()
        ui.setupUi(self.ReportWidget, reports)
        self.ReportWidget.show()

