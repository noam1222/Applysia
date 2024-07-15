from PyQt5.QtWidgets import QDialog, QVBoxLayout, QProgressBar


class ProgressDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Analyzing Progress")
        self.setFixedSize(275, 60)

        layout = QVBoxLayout()

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setRange(0, 100)
        layout.addWidget(self.progress_bar)

        self.setLayout(layout)

    def update_progress(self, progress):
        self.progress_bar.setValue(progress)
