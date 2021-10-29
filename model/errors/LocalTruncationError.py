import copy

import numpy as np
from controller.Input import Input
from model.Function import Function
from model.grids.GridAbscissaX import GridAbscissaX
from model.numerical_methods.NumericalMethodGrid import NumericalMethodGrid


class LocalTruncationError(GridAbscissaX):
    def __init__(self, function : Function, numerical_approximation : NumericalMethodGrid, input : Input, color : str, need_copy=True):
        super().__init__(function, input, color)

        if(need_copy):
            self.numerical_approximation = copy.deepcopy(numerical_approximation)
        else:
            self.numerical_approximation = numerical_approximation
        self.update()
        
    def compute_y(self):
        y_exact = self.function.f_exact(self.x)
        
        x_lte = self.x
        y_lte = np.zeros(len(x_lte))

        # compute the numerical method grid to obtain the LTE
        self.numerical_approximation.__init__(self.function, self.input, self.color)

        for i in range(1, len(x_lte)):
            y_lte[i] = np.abs( y_exact[i] - self.numerical_approximation.y[i] )

        return y_lte
