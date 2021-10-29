from controller.Input import Input

from model.Function import Function
from model.grids.GridAbscissaX import GridAbscissaX


class ExactSolutionGrid(GridAbscissaX):
    def __init__(self, function : Function, input : Input, color : str):
        super().__init__(function, input, color)
        
        self.update()

    def compute_y(self):
        return self.function.f_exact(self.x)
