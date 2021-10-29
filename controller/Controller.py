from model.Model import Model
from view.View import View

from controller.Input import Input
from controller.InputController import InputController
from controller.InputError import InputError


class Controller():
    def __init__(self, model : Model, view : View):
        self.view = view
        self.view.set_controller(self)

        self.input = Input()
        self.input_controller = InputController(self.view, self.input)

        self.update_input()

        self.model = model
        self.model.initialize(self.input)

        # the first plots are built with the program launch
        self.view.on_pb_plot_clicked()

    # the logical core of the "Plot" button
    def update_on_plot(self):
        # step 1: update the input via InputController
        try:
            self.update_input()
        except InputError:
            return

        # step 2: update the model according to the new input
        self.model.update()

        # step 3: update the view
        self.view.update_mplwidgets(self.model, self.input.step_size_warning)

    # updating the input via InputController
    def update_input(self):
        try:
            self.input_controller.update_input()
        except InputError as e:
            self.handle_input_error(e)
            raise
        
    # InputError handler method
    def handle_input_error(self, e : InputError):
        self.view.handle_input_error(e)
        
    