from controller.Input import Input

class Function():
    def __init__(self, f_prime, f_exact_of_C, C_func):
        self.f_prime = f_prime
        self.f_exact_of_C = f_exact_of_C
        self.C_func = C_func

    def set_input(self, input : Input):
        self.input = input

    def update(self):
        x0 = self.input.x0
        y0 = self.input.y0

        self.C = self.C_func(x0, y0)

    def f_exact(self, x : float):
        return self.f_exact_of_C(x, self.C)