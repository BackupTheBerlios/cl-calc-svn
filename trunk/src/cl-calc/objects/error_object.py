# ------------------------------------------------------------------
#
# cl_error.py - The error type
# ------------------------------------------------------------------

import cl_object

class CL_Error(cl_object.CL_Object):
    def __init__(self, message=None, err_code=None):
        self.message = message
        self.err_code = err_code

    def cl_string(self):
        if self.message is not None:
            return self.message
        else:
            return 'Error Occurred!'
