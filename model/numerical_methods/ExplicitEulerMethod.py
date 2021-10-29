import numpy as np
from controller.Input import Input
from model.Function import Function

from model.numerical_methods.NumericalMethodGrid import NumericalMethodGrid


class ExplicitEulerMethod(NumericalMethodGrid):

    def __init__(self, function : Function, input: Input, color: str):
        super().__init__(function, input, color)

        self.update()

    def compute_y(self):
        y = np.zeros(len(self.x))
        y[0] = self.y0

        for i in range(0, len(self.x) - 1):
            y[i+1] = y[i] + self.h * self.function.f_prime(self.x[i], y[i])

        return y
