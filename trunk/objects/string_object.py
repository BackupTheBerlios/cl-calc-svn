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
    
    # binary opts
    def __add__(self, other):
        return CL_String(self.str + to_clstring(other).str)

    def __sub__(self):
        print "String does not support binary sub"

    def __mult__(self):
        print "String does not support binary sub"

    def __div__(self):
        print "String does not support binary sub"

    # comparison
    def __gt__(self, other):
        print "String does not support binary gt"

    def __ge__(self, other):
        print "String does not support binary ge"

    def __lt__(self, other):
        print "String does not support binary lt"

    def __le__(self, other):
        print "String does not support binary le"

    def __eq__(self, other):
        return CL_String(self.str == to_clstring(other).str)

    def __neq__(self, other):
        return CL_String(self.str != to_clstring(other).str)

    def __nonzero__(self):
        return self.str.__nonzero__()

    def __repr__(self):
        return 'CLString(\'%s\')' %(self.str)

    def CL_repr(self):
        return '\'%s\'' %(self.str)

def to_clstring(obj):
    if isinstance(obj, CL_String):
        return obj
    elif isinstance(obj, str):
        return CL_String(obj)
    else:
        return CL_String(str(obj))
