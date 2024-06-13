import sys
from PyQt5 import QtWidgets, QtGui, QtCore

from algo.coordinates import norm_point_to_box
from constants import TRAIL_POINTS_DB, APPLYSIA_DB

Y = (0, 83, 166, 250)
X = (0, 136, 272, 408, 544, 680)

def trail_point_to_point(tp):
    return tp["x"], tp["y"]


def draw_trail_points(x0, y0, box_width, box_height, painter, trail_points):
    p_prev = norm_point_to_box(trail_point_to_point(trail_points[0]), box_width, box_height)
    p_prev = (p_prev[0] + x0, p_prev[1] + y0)
    for p in trail_points[1:]:
        p = norm_point_to_box(trail_point_to_point(p), box_width, box_height)
        p = (p[0] + x0, p[1] + y0)
        painter.drawLine(QtCore.QLineF(p_prev[0], p_prev[1], p[0], p[1]))
        p_prev = p


class AplysiaGridDrawer(QtWidgets.QLabel):
    def __init__(self, reports, parent=None):
        super().__init__(parent)

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

        # Draw Aplysia's numbers
        app = 1
        for j in range(len(Y) - 1):
            for i in range(len(X) - 1):
                # draw app num
                rect = QtCore.QRect(X[i], Y[j], 15, 23)
                painter.setBrush(QtGui.QColor(198, 190, 190, 54))
                painter.setPen(QtGui.QColor(0, 0, 0, 100))
                painter.drawRect(rect)
                painter.setBrush(QtCore.Qt.NoBrush)
                painter.setPen(QtCore.Qt.black)
                painter.drawText(rect, QtCore.Qt.AlignCenter | QtCore.Qt.TextWordWrap, str(app))

                # draw trail
                # TODO fix color and thickness
                # TODO change when specific aplysia?
                for report in reports:
                    if report[APPLYSIA_DB] == app:
                        draw_trail_points(X[i], Y[j], X[i+1]-X[i], Y[j+1]-Y[j], painter, report[TRAIL_POINTS_DB])

                app += 1

        painter.end()

        self.setScaledContents(True)
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setPixmap(pixmap)
