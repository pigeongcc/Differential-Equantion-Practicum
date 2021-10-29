from view.View import View
from controller.Input import Input
from controller.InputError import InputError

class InputController():
    def __init__(self, view : View, input : Input):
        self.view = view
        self.input = input

    def update_input(self):
        # read the input as strings and store it in self.input
        self.read_input()

        try:
            # check if the read strings are numeric
            self.check_if_input_is_numeric()

            self.convert_input_to_numbers()
        
            # check if the input suits the problem conditions
            self.check_if_input_is_correct()
        except InputError:
            raise

        # if the input is correct, the step size still may be >= 1
        # if so, a warning message is printed in the View
        self.check_step_size()

    def read_input(self):
        # applte tab input
        self.input.x0 = self.view.le_x0.text()
        self.input.X = self.view.le_X.text()
        self.input.y0 = self.view.le_y0.text()
        self.input.N = self.view.le_N_applte.text()
        
        # gte tab input
        self.input.n0 = self.view.le_n0.text()
        self.input.N_gte = self.view.le_N_gte.text()
    
    def check_if_input_is_numeric(self):
        # applte tab input
        x0 = self.input.x0
        X = self.input.X
        y0 = self.input.y0
        N = self.input.N

        if not x0.replace('.','',1).isdigit():
            e = InputError("Input error:\n\nx0 must be a positive real number", 1)
            raise e
        if not X.replace('.','',1).isdigit():
            e = InputError("Input error:\n\nX must be a positive real number", 1)
            raise e
        if not y0.replace('.','',1).isdigit():
            e = InputError("Input error:\n\ny0 must be a positive real number", 1)
            raise e
        if not N.isdigit():
            e = InputError("Input error:\n\nN must be a positive integer", 1)
            raise e
        
        # gte tab input
        n0 = self.input.n0
        N_gte = self.input.N_gte
        
        if not n0.isdigit():
            e = InputError("Input error:\n\nn0 must be a positive integer", 2)
            raise e
        if not N_gte.isdigit():
            e = InputError("Input error:\n\nN must be a positive integer", 2)
            raise e

    def convert_input_to_numbers(self):
        # applte tab input
        self.input.x0 = float(self.input.x0)
        self.input.X = float(self.input.X)
        self.input.y0 = float(self.input.y0)
        self.input.N = int(self.input.N)
        
        # gte tab input
        self.input.n0 = int(self.input.n0)
        self.input.N_gte = int(self.input.N_gte)

    def check_if_input_is_correct(self):
        # applte tab input
        x0 = self.input.x0
        X = self.input.X
        y0 = self.input.y0
        N = self.input.N
        
        if x0 <= 0:
            e = InputError("Input error:\n\nx0 is out of the domain of y(x)\n\nx0 > 0", 1)
            raise e
        if x0 >= X:
            e = InputError("Input error:\n x0 must be less than X", 1)
            raise e
        if y0 < x0:
            e = InputError("Input error:\n\ny0 is out of the range\n\ny >= x", 1)
            raise e
        if y0 == 2*x0:
            e = InputError("Input error:\n\nx0 is out of domain\n\ny0 != 2*x0", 1)
            raise e
        if not isinstance(N, int) or N <= 0:
            e = InputError("Input error:\n\nN must be a positive integer", 1)
            raise e
            
        # gte tab input
        n0 = self.input.n0
        N_gte = self.input.N_gte

        if not isinstance(n0, int) or n0 <= 0:
            e = InputError("Input error:\n\nn0 must be a positive integer", 2)
            raise e
        if not isinstance(N_gte, int) or N_gte <= 0:
            e = InputError("Input error:\n\nN must be a positive integer", 2)
            raise e
        if n0 >= N_gte:
            e = InputError("Input error:\n n0 must be less than N", 2)
            raise e

    def check_step_size(self):
        x0 = self.input.x0
        X = self.input.X
        N = self.input.N

        step_size = (X - x0) / N
        if step_size >= 1:
            self.input.step_size_warning = True
        else:
            self.input.step_size_warning = False
