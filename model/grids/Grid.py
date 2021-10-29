from abc import ABC, abstractmethod

from controller.Input import Input
from model.Function import Function


class Grid(ABC):
    def __init__(self, function : Function, input : Input, color : str):
        super().__init__()
        self.function = function
        self.input = input
        self.color = color

        self.update_data()

    def update_data(self):
        self.x0 = self.input.x0
        self.X = self.input.X
        self.y0 = self.input.y0
        self.N = self.input.N

        self.n0 = self.input.n0
        self.N_gte = self.input.N_gte

    @abstractmethod
    def update(self):
        pass
        
    @abstractmethod
    def compute_x(self):
        pass

    @abstractmethod
    def compute_y(self):
        pass
