from PyQt5 import QtWidgets, QtGui, QtCore
from constants import getIconPath
from db.controller import delete_unique_report, delete_all_reports_by_date_and_time


class TrashLabel(QtWidgets.QLabel):
    def __init__(self, parent, libraryWindow):
        super().__init__(parent)
        self.libraryWindow = libraryWindow
        self.setAcceptDrops(True)
        self.setText("")
        self.setPixmap(QtGui.QPixmap(getIconPath("trash_can_icon.png")))
        self.setObjectName("trash")
        self.setScaledContents(True)
        self.setFixedSize(150, 200)
        self.setStyleSheet("margin-bottom: 25px")

    def dragEnterEvent(self, event):
        self.setPixmap(QtGui.QPixmap(getIconPath("red_trash.png")))
        if event.source() in (self.libraryWindow.treeWidget_2, self.libraryWindow.treeWidget):
            event.accept()
        else:
            event.ignore()

    def dragLeaveEvent(self, event):
        self.setPixmap(QtGui.QPixmap(getIconPath("trash_can_icon.png")))

    def dropEvent(self, event):
        self.setPixmap(QtGui.QPixmap(getIconPath("trash_can_icon.png")))
        if event.source() in (self.libraryWindow.treeWidget_2, self.libraryWindow.treeWidget):
            if event.source() ==  self.libraryWindow.treeWidget_2:
                dragged_item = self.libraryWindow.treeWidget_2.currentItem()
            else:
                dragged_item = self.libraryWindow.treeWidget.currentItem()
            if not dragged_item:
                dragged_item = self.libraryWindow.treeWidget.currentItem()
            text = dragged_item.text(0)
            if dragged_item and not self.is_child(text):
                event.accept()
                parent_item = dragged_item.parent()
                if parent_item:
                    parent_text = parent_item.text(0)
                    date = self.libraryWindow.curr_date
                    time = text
                    if parent_text == "All":
                        reply = self.deleteModal("ALL", date, time)
                        if reply == QtWidgets.QMessageBox.Ok:
                            delete_all_reports_by_date_and_time(date, time)
                            self.libraryWindow.filter()
                    else:
                        app_num = self.libraryWindow.get_app_num(parent_text)
                        reply = self.deleteModal(f"applysia {app_num}", date, time)
                        if reply == QtWidgets.QMessageBox.Ok:
                            delete_unique_report(date, time, app_num)
                            self.libraryWindow.filter()
            else:
                event.ignore()
        else:
            event.ignore()

    def is_child(self, text):
        return text[0] == "A"

    def deleteModal(self, app, date, time):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setText(f"This operation will delete {app} reports from:\n" +
                    f"Date: {date}\n" +
                    f"Time: {time}\n" +
                    "Are you sure?")
        msg.setWindowTitle("Warning")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        return msg.exec_()
