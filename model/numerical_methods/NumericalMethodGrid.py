from abc import abstractmethod

from controller.Input import Input
from model.Function import Function
from model.grids.GridAbscissaX import GridAbscissaX


class NumericalMethodGrid(GridAbscissaX):
    def __init__(self, function : Function, input : Input, color : str):
        super().__init__(function, input, color)

        self.f_prime = self.function.f_prime
        self.y : list[float] = []

    @abstractmethod
    def compute_y(self):
        pass
