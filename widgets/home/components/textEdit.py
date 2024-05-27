from PyQt5 import QtWidgets


class TextEdit(QtWidgets.QLineEdit):
    def __init__(self, parent, placeholder, name, readOnly=True):
        super().__init__(parent)

        self.setStyleSheet(
            "padding: 5px;\n"
            "border-radius: 5px;\n"
            "margin-left: 5px;")
        self.setText("")
        self.setPlaceholderText(placeholder)
        self.setReadOnly(readOnly)
        self.setObjectName(name)
