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
            dragged_item = self.libraryWindow.treeWidget_2.currentItem()
            if not dragged_item:
                dragged_item = self.libraryWindow.treeWidget.currentItem()
            text = dragged_item.text(0)
            if dragged_item and not self.is_child(text):
                event.accept()
                parent_item = dragged_item.parent()
                if parent_item:
                    parent_text = parent_item.text(0)
                    if parent_text == "All":
                        # TODO check if work after ari update
                        delete_all_reports_by_date_and_time(self.libraryWindow.curr_date, text)
                        self.libraryWindow.filter()
                    else:
                        app_num = self.libraryWindow.get_app_num(parent_text)
                        delete_unique_report(self.libraryWindow.curr_date, text, app_num)
                        parent_item.removeChild(dragged_item)
            else:
                # TODO add remove all applysia reports
                event.ignore()
        else:
            event.ignore()

    def is_child(self, text):
        return text[0] == "A"

