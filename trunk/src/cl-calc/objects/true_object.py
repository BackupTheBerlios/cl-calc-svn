# ------------------------------------------------------------------
#
# true_object.py - true object
# ------------------------------------------------------------------


import cl_object

class CL_True(cl_object.CL_Object):
    def __init__(self):
        pass

    def __repr__(self):
        return 'CL_True()'

    def CL_repr(self):
        return 'True'
