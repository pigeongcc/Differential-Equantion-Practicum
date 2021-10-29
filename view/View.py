from ui.ui import Ui_Form
from controller.InputError import InputError
from matplotlib.backends.backend_qt5agg import \
    FigureCanvasQTAgg as FigureCanvasQTAgg
from model.grids.Grid import Grid
from model.Model import Model
from PyQt5.QtWidgets import QVBoxLayout, QWidget

from view.MplWidget import MplWidget


class View(QWidget, Ui_Form):
    # initialize the GUI
    def __init__(self):
        super(View, self).__init__()
        self.setupUi(self)

        #initialize matplotlib widgets
        self.init_mplwidgets()

        # connect the "Plot" buttons to the plotting (model updating) method
        self.pb_plot_applte.clicked.connect(self.on_pb_plot_clicked)
        self.pb_plot_gte.clicked.connect(self.on_pb_plot_clicked)

    def set_controller(self, controller):
        self.controller = controller

    def init_mplwidgets(self):
        self.mplwidget_app = MplWidget()
        self.vl_app = QVBoxLayout(self.app_plot)
        self.vl_app.addWidget(self.mplwidget_app)
        
        self.mplwidget_lte = MplWidget()
        self.vl_lte = QVBoxLayout(self.lte_plot)
        self.vl_lte.addWidget(self.mplwidget_lte)
        
        self.mplwidget_gte = MplWidget()
        self.vl_gte = QVBoxLayout(self.gte_plot)
        self.vl_gte.addWidget(self.mplwidget_gte)

    def on_pb_plot_clicked(self):
        self.controller.update_on_plot()

    def update_mplwidgets(self, model : Model, step_size_warning : bool):

        tab_index = self.tabWidget.currentIndex()
        self.clear_mplwidgets(tab_index)
        
        if tab_index == 0:
            # approximations
            if self.cb_exact.isChecked():
                self.plot(self.mplwidget_app, model.exact_solution)
            if self.cb_eem.isChecked():
                self.plot(self.mplwidget_app, model.eem)
            if self.cb_iem.isChecked():
                self.plot(self.mplwidget_app, model.iem)
            if self.cb_rkm.isChecked():
                self.plot(self.mplwidget_app, model.rkm)
            # LTEs
            if self.cb_eem_lte.isChecked():
                self.plot(self.mplwidget_lte, model.lte_eem)
            if self.cb_iem_lte.isChecked():
                self.plot(self.mplwidget_lte, model.lte_iem)
            if self.cb_rkm_lte.isChecked():
                self.plot(self.mplwidget_lte, model.lte_rkm)
            
            self.label_applte.setText("Plotted successfully")
            if step_size_warning is True:
                self.label_applte.setText("Plotted successfully\n\nWarning:\nstep size is >= 1")

        elif tab_index == 1: 
            # GTEs
            if self.cb_eem_gte.isChecked():
                self.plot(self.mplwidget_gte, model.gte_eem)
            if self.cb_iem_gte.isChecked():
                self.plot(self.mplwidget_gte, model.gte_iem)
            if self.cb_rkm_gte.isChecked():
                self.plot(self.mplwidget_gte, model.gte_rkm)
                
            self.label_gte.setText("Plotted successfully")
        
    def plot(self, mplwidget : MplWidget, grid : Grid):
        mplwidget.axis.plot(grid.x, grid.y, grid.color)
        mplwidget.canvas.draw()

    def handle_input_error(self, e : InputError):
        # determining on which tab the error occurred
        if e.tab_number == 1:
            label = self.label_applte
        elif e.tab_number == 2:
            label = self.label_gte
        
        # printing an error message
        label.setText(e.message)

        self.clear_mplwidgets()

    # the method clears the matplotlib widgets
    def clear_mplwidgets(self, tab='all'):
        if tab == 0 or tab == 'all':
            self.mplwidget_app.axis.clear()  
            self.mplwidget_lte.axis.clear()
        if tab == 1 or tab == 'all':
            self.mplwidget_gte.axis.clear()
