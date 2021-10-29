class Error(Exception):
    pass

class InputError(Error):
    """
    Exception raised for errors in the input.

    Attributes:
        message -- explanation of the error
        tab_number -- number of tab at which the error occured
    """
    
    def __init__(self, message, tab_number):
        self.message = message
        self.tab_number = tab_number