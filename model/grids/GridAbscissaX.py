from abc import abstractmethod

import numpy as np
from controller.Input import Input
from model.Function import Function

from model.grids.Grid import Grid


class GridAbscissaX(Grid):
    def __init__(self, function : Function, input : Input, color : str):
        super().__init__(function, input, color)

        self.update_data()

    def update(self):
        self.update_data()
        self.h = self.compute_h()
        self.x = self.compute_x()
        self.y = self.compute_y()
        
    def compute_h(self):
        return (self.X - self.x0) / self.N

    def compute_x(self):
        # to get N grid cells we need to plot N+1 points
        return np.linspace(self.x0, self.X, self.N+1)

    @abstractmethod
    def compute_y(self):
        pass
