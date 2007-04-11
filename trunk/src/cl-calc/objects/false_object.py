# ------------------------------------------------------------------
#
# false_object.py - false object
# ------------------------------------------------------------------


import cl_object

class CL_False(cl_object.CL_Object):
    def __init__(self):
        pass

    def __repr__(self):
        return 'CL_False()'

    def CL_repr(self):
        return 'False'
