import sys

import numpy as np
from PyQt5.QtWidgets import QApplication

from controller.Controller import Controller
from model.Function import Function
from model.Model import Model
from view.View import View

sys.path.insert(0, 'C:\\Users\\gulya\\Desktop\\DE')
sys.path.insert(0, 'C:\\Users\\gulya\\Desktop\\DE\\controller')
sys.path.insert(0, 'C:\\Users\\gulya\\Desktop\\DE\\model')
sys.path.insert(0, 'C:\\Users\\gulya\\Desktop\\DE\\ui')
sys.path.insert(0, 'C:\\Users\\gulya\\Desktop\\DE\\view')

# initialization of the program elements and launching the view
if __name__ == '__main__':
    # initialization of Function
    # f_prime = y'(x,y)
    f_prime = lambda x, y: np.sqrt(y-x) / np.sqrt(x) + 1
    # formula for C
    C = lambda x, y: (np.sqrt(x) + np.sqrt(y-x) ) / (2*x - y)
    # f_exact = y(x, C)
    f_exact = lambda x, C: 2 * x - 2 * np.sqrt(x) / C + 1 / C**2

    function_variant_30 = Function(f_prime, f_exact, C)

    # initialization of Model
    model = Model(function_variant_30)

    # initialization of View
    app = QApplication(sys.argv)
    view = View()

    # initialization of Controller
    controller = Controller(model, view)
    
    # launching the View
    view.show()
    sys.exit(app.exec_())
