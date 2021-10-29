from matplotlib.backends.backend_qt5agg import \
    FigureCanvasQTAgg as FigureCanvasQTAgg
from matplotlib.backends.backend_qt5agg import \
    NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from PyQt5.QtWidgets import QVBoxLayout, QWidget


class MplWidget(QWidget):
    def __init__(self, parent=None):
        super(MplWidget, self).__init__(parent)

        self.figure = Figure()
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.axis = self.figure.add_subplot(111)
        self.toolbar = NavigationToolbar(self.canvas, self)

        self.vl = QVBoxLayout(self)
        self.vl.addWidget(self.toolbar)
        self.vl.addWidget(self.canvas)
