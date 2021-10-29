from abc import abstractmethod

import numpy as np
from controller.Input import Input
from model.Function import Function

from model.grids.Grid import Grid


class GridAbscissaN(Grid):
    def __init__(self, function : Function, input : Input, color : str):
        super().__init__(function, input, color)

        #self.x = self.compute_x()
        self.update_data()

    def update(self):
        self.update_data()
        self.compute_x()
        self.compute_y()

    def compute_x(self):
        # range for X axis is [n0; N] with step 1 (natural numbers only)
        return np.arange(self.n0, self.N_gte+1, 1)

    @abstractmethod
    def compute_y(self):
        pass
