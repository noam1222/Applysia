from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ReportWidget(object):
    def setupUi(self, ReportWidget):
        ReportWidget.setObjectName("ReportWidget")
        ReportWidget.setFixedSize(721, 761)

        self.verticalLayoutWidget = QtWidgets.QWidget(ReportWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 721, 761))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.mainVerticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.mainVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.mainVerticalLayout.setObjectName("mainVerticalLayout")

        # Headline
        self.headLineHorizontalLayout = QtWidgets.QHBoxLayout()
        self.headLineHorizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.headLineHorizontalLayout.setContentsMargins(6, -1, 6, 0)
        self.headLineHorizontalLayout.setObjectName("headLineHorizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, -1, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.headLineHorizontalLayout.addItem(spacerItem)
        self.headlineLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(40)
        self.headlineLabel.setFont(font)
        self.headlineLabel.setObjectName("headlineLabel")
        self.headLineHorizontalLayout.addWidget(self.headlineLabel)
        spacerItem1 = QtWidgets.QSpacerItem(40, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.headLineHorizontalLayout.addItem(spacerItem1)
        self.mainVerticalLayout.addLayout(self.headLineHorizontalLayout)

        # Info line
        self.infoHorizontalLayout = QtWidgets.QHBoxLayout()
        self.infoHorizontalLayout.setContentsMargins(20, -1, 6, -1)
        self.infoHorizontalLayout.setObjectName("dateHorizontalLayout")
        spacerItem4 = QtWidgets.QSpacerItem(40, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
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
        spacerItem3 = QtWidgets.QSpacerItem(40, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.infoHorizontalLayout.addItem(spacerItem3)
        
        self.ApplysiaToShowLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Narkisim")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.ApplysiaToShowLabel.setFont(font)
        self.ApplysiaToShowLabel.setObjectName("ApplysiaToShowLabel")
        self.infoHorizontalLayout.addWidget(self.ApplysiaToShowLabel)
        self.ApplysiaToShowComboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.ApplysiaToShowComboBox.setStyleSheet("border-radius: 10px;\n"
"background: white;\n"
"border: 1px solid gray;\n"
"padding: 4px 4px 4px 4px;")
        self.ApplysiaToShowComboBox.setObjectName("ApplysiaToShowComboBox")
        self.ApplysiaToShowComboBox.addItem("")
        self.ApplysiaToShowComboBox.addItem("")
        self.ApplysiaToShowComboBox.addItem("")
        self.ApplysiaToShowComboBox.addItem("")
        self.ApplysiaToShowComboBox.addItem("")
        self.ApplysiaToShowComboBox.addItem("")
        self.ApplysiaToShowComboBox.addItem("")
        self.ApplysiaToShowComboBox.addItem("")
        self.ApplysiaToShowComboBox.addItem("")
        self.ApplysiaToShowComboBox.addItem("")
        self.infoHorizontalLayout.addWidget(self.ApplysiaToShowComboBox)
        spacerItem2 = QtWidgets.QSpacerItem(40, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.infoHorizontalLayout.addItem(spacerItem2)
        self.mainVerticalLayout.addLayout(self.infoHorizontalLayout)

        # Movement table
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
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

        pixmap = QtGui.QPixmap(680, 250)
        pixmap.fill(QtCore.Qt.white)
        painter = QtGui.QPainter(pixmap)
        pen = QtGui.QPen(QtCore.Qt.black, 2, QtCore.Qt.SolidLine)
        painter.setPen(pen)
        # Divide horizontally
        painter.drawLine(0, 83, 680, 83)
        painter.drawLine(0, 166, 680, 166)
        # Divide vertically
        painter.drawLine(136, 0, 136, 250)
        painter.drawLine(272, 0, 272, 250)
        painter.drawLine(408, 0, 408, 250)
        painter.drawLine(544, 0, 544, 250)
        painter.end()

        self.canvas = QtWidgets.QLabel()
        self.canvas.setScaledContents(True)
        self.canvas.setAlignment(QtCore.Qt.AlignCenter)
        self.canvas.setPixmap(pixmap)

        self.drawerHorizontalLayout.addWidget(self.canvas)
        self.mainVerticalLayout.addLayout(self.drawerHorizontalLayout)

        # Export
        self.exportHorizontalLayout = QtWidgets.QHBoxLayout()
        self.exportHorizontalLayout.setContentsMargins(20, 20, 20, 30)
        self.exportHorizontalLayout.setSpacing(6)
        self.exportHorizontalLayout.setObjectName("exportHorizontalLayout")

        self.exportExcel = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.exportExcel.setStyleSheet("background: rgba(152, 113, 113, 150);\n"
"border-radius: 10px 10px 10px 10px;")
        self.exportExcel.setObjectName("exportExcel")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.exportExcel)
        self.horizontalLayout_5.setContentsMargins(-1, 5, 7, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.label_9 = QtWidgets.QLabel(self.exportExcel)
        self.label_9.setStyleSheet("background: transparent;")
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("res/icons/excel_logo_icon.png"))
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
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
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.exportHorizontalLayout.addWidget(self.exportExcel)

        self.exportWord = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.exportWord.setStyleSheet("background: rgba(152, 113, 113, 150);\n"
"border-radius: 10px 10px 10px 10px;")
        self.exportWord.setObjectName("exportWord")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.exportWord)
        self.horizontalLayout_4.setContentsMargins(-1, 5, 7, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem5 = QtWidgets.QSpacerItem(40, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.label_7 = QtWidgets.QLabel(self.exportWord)
        self.label_7.setStyleSheet("background: transparent;")
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("res/icons/word_logo_icon.png"))
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
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
        spacerItem6 = QtWidgets.QSpacerItem(40, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.exportHorizontalLayout.addWidget(self.exportWord)

        self.exportVideo = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.exportVideo.setStyleSheet("background: rgba(152, 113, 113, 150);\n"
"border-radius: 10px 10px 10px 10px;")
        self.exportVideo.setObjectName("exportVideo")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.exportVideo)
        self.horizontalLayout.setContentsMargins(-1, 7, 7, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.label_6 = QtWidgets.QLabel(self.exportVideo)
        self.label_6.setStyleSheet("background: transparent;")
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("res/icons/video_icon.png"))
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
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
        self.horizontalLayout.addWidget(self.label_5, 0, QtCore.Qt.AlignHCenter)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem8)
        self.exportHorizontalLayout.addWidget(self.exportVideo)
        self.mainVerticalLayout.addLayout(self.exportHorizontalLayout)

        self.retranslateUi(ReportWidget)
        QtCore.QMetaObject.connectSlotsByName(ReportWidget)

    def retranslateUi(self, ReportWidget):
        _translate = QtCore.QCoreApplication.translate
        ReportWidget.setWindowTitle(_translate("ReportWidget", "Form"))
        self.headlineLabel.setText(_translate("ReportWidget", "Report #12"))
        self.dateLabel.setText(_translate("ReportWidget", "Date: 10/12/21"))
        self.ApplysiaToShowLabel.setText(_translate("ReportWidget", "Applysia:"))
        self.ApplysiaToShowComboBox.setItemText(0, _translate("ReportWidget", "All"))
        self.ApplysiaToShowComboBox.setItemText(1, _translate("ReportWidget", "1"))
        self.ApplysiaToShowComboBox.setItemText(2, _translate("ReportWidget", "2"))
        self.ApplysiaToShowComboBox.setItemText(3, _translate("ReportWidget", "3"))
        self.ApplysiaToShowComboBox.setItemText(4, _translate("ReportWidget", "4"))
        self.ApplysiaToShowComboBox.setItemText(5, _translate("ReportWidget", "5"))
        self.ApplysiaToShowComboBox.setItemText(6, _translate("ReportWidget", "6"))
        self.ApplysiaToShowComboBox.setItemText(7, _translate("ReportWidget", "7"))
        self.ApplysiaToShowComboBox.setItemText(8, _translate("ReportWidget", "8"))
        self.ApplysiaToShowComboBox.setItemText(9, _translate("ReportWidget", "9"))
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
        item.setText(_translate("ReportWidget", "Period"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("ReportWidget", "Movement"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("ReportWidget", "Period"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("ReportWidget", "Movement"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label_10.setText(_translate("ReportWidget", "Export to Excel"))
        self.label_8.setText(_translate("ReportWidget", "Export to Word"))
        self.label_5.setText(_translate("ReportWidget", "Create routes video"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ReportWidget = QtWidgets.QWidget()
    ui = Ui_ReportWidget()
    ui.setupUi(ReportWidget)
    ReportWidget.show()
    sys.exit(app.exec_())
