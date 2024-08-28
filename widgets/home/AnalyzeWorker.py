from PyQt5.QtCore import QThread, pyqtSignal
from algo.analyze import analyze


class AnalyzeWorker(QThread):
    progress = pyqtSignal(int)
    finished = pyqtSignal(dict)

    def __init__(self, video_path, video_speed):
        super().__init__()
        self.video_path = video_path
        self.video_speed = video_speed

    def run(self):
        results = analyze(self.video_path, self.video_speed, self.progress.emit)
        self.finished.emit(results)
