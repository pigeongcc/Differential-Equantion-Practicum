import copy as copy

import numpy as np
from controller.Input import Input
from model.Function import Function
from model.grids.GridAbscissaN import GridAbscissaN
from model.numerical_methods.NumericalMethodGrid import NumericalMethodGrid

from model.errors.LocalTruncationError import LocalTruncationError


class GlobalTruncationError(GridAbscissaN):
    def __init__(self, function : Function, numerical_approximation : NumericalMethodGrid, input : Input, color : str):
        super().__init__(function, input, color)

        self.numerical_approximation = numerical_approximation
        self.input = input

        self.update()

    def update(self):
        self.update_data()
        self.x = self.compute_x()
        self.y = self.compute_y()

    def compute_y(self):
        y_gte = np.zeros(len(self.x))

        for i in range(len(self.x)):
            # compute LTE for a given approximation
            
            # copy the current input
            input = copy.deepcopy(self.input)
            # change N parameter
            input.N = self.x[i]
            # pass this modified input to the LTE
            self.numerical_approximation.__init__(self.function, input, self.color)
            # compute LTE
            lte = LocalTruncationError(self.function, self.numerical_approximation, input, self.color, False)

            # assign GTE for a given N
            y_gte[i] = max(lte.y)

        return y_gte
