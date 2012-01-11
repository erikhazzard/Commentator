'''=======================================================================

    Errors.py
    =====================================

    =====================================
    description 
        This file contains commentator's custom error classes, used for
        error handling
    =====================================

    ====================================================================== '''
class MissingParameter(Exception):
    def __init__(self, value):
        self.parameter = value

    def __str__(self):
        print self.parameter
        #return repr(self.parameter)
