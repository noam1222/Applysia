import copy

from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import timedelta

from constants import *
from widgets.report.drawer import AplysiaGridDrawer
from .exports import *

class Ui_ReportWidget(object):
    def setupUi(self, ReportWidget, reports, current_aplysia=0):
        ReportWidget.setObjectName("ReportWidget")
        ReportWidget.setWindowIcon(QtGui.QIcon(getImgPath("vision.png")))
        ReportWidget.setFixedSize(721, 761)

        self.reports = reports
        self.curr_app = current_aplysia
        self.report_widget = ReportWidget

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 253, 208))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 125, 105))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 253, 208))
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 125, 105))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 253, 208))
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 125, 105))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 253, 208))
        brush.setStyle(QtCore.Qt.SolidPattern)
        ReportWidget.setPalette(palette)

        self.verticalLayoutWidget = QtWidgets.QWidget(ReportWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 721, 761))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.mainVerticalLayout = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget)
        self.mainVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.mainVerticalLayout.setObjectName("mainVerticalLayout")

        # Headline
        self.headLineHorizontalLayout = QtWidgets.QHBoxLayout()
        self.headLineHorizontalLayout.setSizeConstraint(
            QtWidgets.QLayout.SetFixedSize)
        self.headLineHorizontalLayout.setContentsMargins(6, -1, 6, 0)
        self.headLineHorizontalLayout.setObjectName("headLineHorizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(
            40, -1, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.headLineHorizontalLayout.addItem(spacerItem)
        self.headlineLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(40)
        self.headlineLabel.setFont(font)
        self.headlineLabel.setObjectName("headlineLabel")
        self.headLineHorizontalLayout.addWidget(self.headlineLabel)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.headLineHorizontalLayout.addItem(spacerItem1)
        self.mainVerticalLayout.addLayout(self.headLineHorizontalLayout)

        # Info line
        self.infoHorizontalLayout = QtWidgets.QHBoxLayout()
        self.infoHorizontalLayout.setContentsMargins(20, -1, 6, -1)
        self.infoHorizontalLayout.setObjectName("dateHorizontalLayout")
        spacerItem4 = QtWidgets.QSpacerItem(
            40, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.infoHorizontalLayout.addItem(spacerItem4)
        self.dateLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Narkisim")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.dateLabel.setFont(font)
        self.dateLabel.setObjectName("dateLabel")
        self.infoHorizontalLayout.addWidget(self.dateLabel)
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.infoHorizontalLayout.addItem(spacerItem3)

        self.movementLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Narkisim")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.movementLabel.setFont(font)
        self.movementLabel.setObjectName("movemntLabel")
        self.infoHorizontalLayout.addWidget(self.movementLabel)
        spacerItem34 = QtWidgets.QSpacerItem(
            40, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.infoHorizontalLayout.addItem(spacerItem34)

        self.ApplysiaToShowLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Narkisim")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.ApplysiaToShowLabel.setFont(font)
        self.ApplysiaToShowLabel.setObjectName("ApplysiaToShowLabel")
        self.infoHorizontalLayout.addWidget(self.ApplysiaToShowLabel)
        self.ApplysiaToShowComboBox = QtWidgets.QComboBox(
            self.verticalLayoutWidget)
        self.ApplysiaToShowComboBox.setStyleSheet("border-radius: 10px;\n"
                                                  "background: white;\n"
                                                  "border: 1px solid gray;\n"
                                                  "padding: 4px 4px 4px 4px;")
        self.ApplysiaToShowComboBox.setObjectName("ApplysiaToShowComboBox")
        for report in reports:
                if report[APPLYSIA_DB] == ALL_APPLYSIAS:
                        self.ApplysiaToShowComboBox.addItem("All")
                else:
                    self.ApplysiaToShowComboBox.addItem(str(report[APPLYSIA_DB]))
        self.infoHorizontalLayout.addWidget(self.ApplysiaToShowComboBox)
        self.ApplysiaToShowComboBox.currentIndexChanged.connect(lambda index: self.app_index_changed(index))

        spacerItem2 = QtWidgets.QSpacerItem(
            40, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.infoHorizontalLayout.addItem(spacerItem2)
        self.mainVerticalLayout.addLayout(self.infoHorizontalLayout)

        # Movement table
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(500, 260))
        self.tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setGridStyle(QtCore.Qt.DashLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(7)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        for i in range(4):
                item = QtWidgets.QTableWidgetItem()
                font = QtGui.QFont()
                font.setPointSize(9)
                font.setBold(True)
                font.setWeight(75)
                item.setFont(font)
                brush = QtGui.QBrush(QtGui.QColor(165, 165, 165))
                brush.setStyle(QtCore.Qt.SolidPattern)
                item.setBackground(brush)
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(0, i, item)
        start_hour = self.reports[self.curr_app][TIME_DB]
        five_min_counter = 0
        for j in (0, 2):
             for i in range(1, 7):
                item = QtWidgets.QTableWidgetItem()
                time = (start_hour + timedelta(minutes=five_min_counter)).time()
                five_min_counter += 5
                item.setText(str(time)[:-3])
                font = QtGui.QFont()
                font.setBold(True)
                font.setPointSize(8)
                item.setFont(font)
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(i, j, item)
        if self.curr_app != 0:
            self.ApplysiaToShowComboBox.setCurrentIndex(self.curr_app)
        else:
            self.set_movement5()

        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.horizontalLayout_2.addWidget(self.tableWidget)
        self.mainVerticalLayout.addLayout(self.horizontalLayout_2)

        # Draw canvas
        self.drawerHorizontalLayout = QtWidgets.QHBoxLayout()
        self.drawerHorizontalLayout.setContentsMargins(20, -1, 20, -1)
        self.drawerHorizontalLayout.setObjectName("drawHorizontalLayout")

        self.canvas = AplysiaGridDrawer(reports=self.reports)

        self.drawerHorizontalLayout.addWidget(self.canvas)
        self.mainVerticalLayout.addLayout(self.drawerHorizontalLayout)

        # Export
        self.exportHorizontalLayout = QtWidgets.QHBoxLayout()
        self.exportHorizontalLayout.setContentsMargins(20, 20, 20, 30)
        self.exportHorizontalLayout.setSpacing(6)
        self.exportHorizontalLayout.setObjectName("exportHorizontalLayout")

        self.exportExcel = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.exportExcel.setStyleSheet("""
            QFrame {
               background: #a2c85e;;
               border-radius: 10px 10px 10px 10px;
            }
            QFrame:hover {
                background: #acbe94;
            }
        """)
        self.exportExcel.mousePressEvent = self.export_excel_clicked
        self.exportExcel.setObjectName("exportExcel")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.exportExcel)
        self.horizontalLayout_5.setContentsMargins(-1, 5, 7, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.label_9 = QtWidgets.QLabel(self.exportExcel)
        self.label_9.setStyleSheet("background: transparent;")
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("res/icons/excel_logo_icon.png"))
        self.label_9.setAlignment(QtCore.Qt.AlignRight |QtCore.Qt.AlignTrailing |QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_5.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.exportExcel)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background: transparent;")
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_5.addWidget(self.label_10)
        spacerItem4 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.exportHorizontalLayout.addWidget(self.exportExcel)

        self.exportWord = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.exportWord.setStyleSheet("""
                    QFrame {
                       background: #5356ea;;
                       border-radius: 10px 10px 10px 10px;
                    }
                    QFrame:hover {
                        background: #b1b4f4;
                    }
                """)
        self.exportWord.setObjectName("exportWord")
        self.exportWord.mousePressEvent = self.export_word_clicked
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.exportWord)
        self.horizontalLayout_4.setContentsMargins(-1, 5, 7, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem5 = QtWidgets.QSpacerItem(
            40, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.label_7 = QtWidgets.QLabel(self.exportWord)
        self.label_7.setStyleSheet("background: transparent;")
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("res/icons/word_logo_icon.png"))
        self.label_7.setAlignment(QtCore.Qt.AlignRight |QtCore.Qt.AlignTrailing |QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.exportWord)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background: transparent;")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_4.addWidget(self.label_8)
        spacerItem6 = QtWidgets.QSpacerItem(
            40, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.exportHorizontalLayout.addWidget(self.exportWord)

        self.exportVideo = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.exportVideo.setStyleSheet("""
                            QFrame {
                               background: #e74b54;;
                               border-radius: 10px 10px 10px 10px;
                            }
                            QFrame:hover {
                                background: #ef848a;
                            }
                        """)
        self.exportVideo.setObjectName("exportVideo")
        self.exportVideo.mousePressEvent = self.export_video_clicked
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.exportVideo)
        self.horizontalLayout.setContentsMargins(-1, 7, 7, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem7 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.label_6 = QtWidgets.QLabel(self.exportVideo)
        self.label_6.setStyleSheet("background: transparent;")
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("res/icons/video_icon.png"))
        self.label_6.setAlignment(QtCore.Qt.AlignRight |QtCore.Qt.AlignTrailing |QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.label_5 = QtWidgets.QLabel(self.exportVideo)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background: transparent;")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(
            self.label_5, 0, QtCore.Qt.AlignHCenter)
        spacerItem8 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem8)
        self.exportHorizontalLayout.addWidget(self.exportVideo)
        self.mainVerticalLayout.addLayout(self.exportHorizontalLayout)

        self.retranslateUi(ReportWidget)
        QtCore.QMetaObject.connectSlotsByName(ReportWidget)

    def retranslateUi(self, ReportWidget):
        _translate = QtCore.QCoreApplication.translate
        ReportWidget.setWindowTitle(_translate("ReportWidget", "Report"))
        self.headlineLabel.setText(_translate("ReportWidget", "Report"))
        self.dateLabel.setText(_translate(
            "ReportWidget", f"Date: {self.reports[0][DATE_DB]}"))
        self.movementLabel.setText(_translate(
            "ReportWidget", f"Movement: {self.reports[self.curr_app][MOVEMENT_DB]:.2f}"))
        self.ApplysiaToShowLabel.setText(
            _translate("ReportWidget", "Applysia:"))

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ReportWidget", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ReportWidget", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("ReportWidget", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("ReportWidget", "New Column"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("ReportWidget", "Time"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("ReportWidget", "Movement"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("ReportWidget", "Time"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("ReportWidget", "Movement"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label_10.setText(_translate("ReportWidget", "Export to Excel"))
        self.label_8.setText(_translate("ReportWidget", "Export to Word"))
        self.label_5.setText(_translate("ReportWidget", "Create routes video"))

    def app_index_changed(self, index):
        self.curr_app = index
        self.movementLabel.setText(f"Movement: {self.reports[index][MOVEMENT_DB]:.2f}")
        self.set_movement5()

    def set_movement5(self):
        counter5 = 0
        for j in (1, 3):
            for i in range(1, 7):
                item = QtWidgets.QTableWidgetItem()
                item.setText(f"{self.reports[self.curr_app][MVMNT5_DB][counter5]:.2f}")
                counter5 += 1
                font = QtGui.QFont()
                font.setPointSize(8)
                item.setFont(font)
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(i, j, item)

    def get_file_path(self, e_type):
        app_num = self.reports[self.curr_app][APPLYSIA_DB]
        curr_app_str = "all" if self.curr_app == 0 else f"app{app_num}"

        time = f"{self.reports[self.curr_app][TIME_DB]}".split(' ')[1].replace(":", "-")
        date_time = f"{self.reports[self.curr_app][DATE_DB]} {time}".replace("/", "-")

        file_name = f"{curr_app_str} {date_time}"

        if e_type == "Excel":
            type_str = "xlsx"
        elif e_type == "Word":
            type_str = "docx"
        elif e_type == "Video":
            type_str = "gif"
        else:
            return

        options = QtWidgets.QFileDialog.Options()
        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(self.report_widget, f"Export to {e_type}", file_name,
                                                            f"{e_type} Files (*.{type_str});;All Files (*)",
                                                            options=options)
        return file_path

    def export_excel_clicked(self, e):
        file_path = self.get_file_path("Excel")
        if not file_path:
            return
        export_report_to_excel(self.reports[self.curr_app], file_path)

    def export_word_clicked(self, e):
        file_path = self.get_file_path("Word")
        if not file_path:
            return
        export_report_to_word(self.reports[self.curr_app], file_path)

    def export_video_clicked(self, e):
        if self.curr_app == 0:
            QtWidgets.QMessageBox.information(self.report_widget, "Ooops..",
                                              "There are no support for multiple applysias movement video.")
            return
        file_path = self.get_file_path("Video")
        if not file_path:
            return
        draw_path_video(self.reports[self.curr_app], file_path)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ReportWidget = QtWidgets.QWidget()
    ui = Ui_ReportWidget()
    ui.setupUi(ReportWidget)
    ReportWidget.show()
    sys.exit(app.exec_())
