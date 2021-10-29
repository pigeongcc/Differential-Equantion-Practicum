from controller.Input import Input

from model.errors.GlobalTruncationError import GlobalTruncationError
from model.errors.LocalTruncationError import LocalTruncationError
from model.ExactSolutionGrid import ExactSolutionGrid
from model.Function import Function
from model.grids.Grid import Grid
from model.numerical_methods.ExplicitEulerMethod import ExplicitEulerMethod
from model.numerical_methods.ImprovedEulerMethod import ImprovedEulerMethod
from model.numerical_methods.RungeKuttaMethod import RungeKuttaMethod


class Model():
    def __init__(self, function : Function):
        self.function = function
        self.graphs : list[Grid] = []
        self.ltes : list[Grid] = []
        self.gtes : list[Grid] = []

    def initialize(self, input : Input):
        self.function.set_input(input)
        self.function.update()
        self.exact_solution = ExactSolutionGrid(self.function, input, 'blue')
        self.graphs.append(self.exact_solution)

        self.eem = ExplicitEulerMethod(self.function, input, 'black')
        self.graphs.append(self.eem)
        self.lte_eem = LocalTruncationError(self.function, self.eem, input, 'black')
        self.graphs.append(self.lte_eem)
        self.gte_eem = GlobalTruncationError(self.function, self.eem, input, 'black')
        self.graphs.append(self.gte_eem)
        
        self.iem = ImprovedEulerMethod(self.function, input, 'red')
        self.ltes.append(self.iem)
        self.lte_iem = LocalTruncationError(self.function, self.iem, input, 'red')
        self.ltes.append(self.lte_iem)
        self.gte_iem = GlobalTruncationError(self.function, self.iem, input, 'red')
        self.ltes.append(self.gte_iem)

        self.rkm = RungeKuttaMethod(self.function, input, 'green')
        self.gtes.append(self.rkm)
        self.lte_rkm = LocalTruncationError(self.function, self.rkm, input, 'green')
        self.gtes.append(self.lte_rkm)
        self.gte_rkm = GlobalTruncationError(self.function, self.rkm, input, 'green')
        self.gtes.append(self.gte_rkm)

    # update() method re-computes the grids according to the actual input
    def update(self):
        self.function.update()
        for grid in self.graphs:
            grid.update()
        for grid in self.ltes:
            grid.update()
        for grid in self.gtes:
            grid.update()
