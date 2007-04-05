# ------------------------------------------------------------------
#
# cl_object.py - Base cl_object type.
# ------------------------------------------------------------------

import cl_type

class CL_Object(object):
    '''CL_Object will only define default object methods as well and store its
    type.  Keeping count of reference count and name will be functions of the
    stack itself.'''
    def __init__(self, name=None, type_obj=cl_type.Object_Type):
        self.type_obj = cl_type.CL_Type(type_obj)

    def __repr__(self):
        return '<Object CL_Object {refcount: %s; name: %s; type: %s;}>' \
            %(self.refcount, self.name, self.type_obj)

    # binary opts
    def __add__(self):
        print "Object does not support binary add"

    def __sub__(self):
        print "Object does not support binary sub"

    def __mult__(self):
        print "Object does not support binary mult"

    def __div__(self):
        print "Object does not support binary div"

    # comparison
    def __gt__(self, other):
        print "Object does not support comparison"

    def __ge__(self, other):
        print "Object does not support comparison"

    def __lt__(self, other):
        print "Object does not support comparison"

    def __le__(self, other):
        print "Object does not support comparison"

    def __eq__(self, other):
        print "Object does not support comparison"

    def __neq__(self, other):
        print "Object does not support comparison"

    def __nonzero__(self):
        print "Object does not support comparison"

    # CL specific methods
    def CL_repr(self):
        return self.__repr__()

