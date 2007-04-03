# ------------------------------------------------------------------
# 
# cl_string.py - the CLString type.  Another wrapper
# ------------------------------------------------------------------

import sys
import os.path

import cl_object

class CL_String(cl_object.CL_Object):
    def __init__(self, string):
        self.str = string
    
    def __repr__(self):
        return 'CLString(\'%s\')' %(self.str)

    def CL_repr(self):
        return self.str
