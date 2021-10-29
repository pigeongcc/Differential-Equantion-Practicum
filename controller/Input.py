# the Input class contains information used by the Model
class Input():
    def __init__(self):
        # applte tab input variables
        self.x0 = -1
        self.X = -1
        self.y0 = -1
        self.N = -1
        
        # gte tab input variables
        self.n0 = -1
        self.N_gte = -1

        # warning flag for notifying about h >= 1 case
        self.step_size_warning = False