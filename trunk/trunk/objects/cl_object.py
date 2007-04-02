# ------------------------------------------------------------------
#
# cl_object.py - Base cl_object type.
# ------------------------------------------------------------------

import cl_type

class CL_Object(object):
    '''Base Object Type.  CL_Object has three attributes:
        1. Refcount - For pseudo garbage collection
        2. Name - Variable Name
        3. Type - Object Type
     
     This class also defines two methods:
         1. inc_ref - Increment References (GC)
         2. dec_ref - GC
         
     Methods beginning with CL_* represent special methods for the cl-calc
     language:
         1. CL_repr - representation in the language.  Please note that the
         __repr__ method is also defined, but this is only for debugging
         purposes.'''
    def __init__(self, name=None, type_obj=cl_type.Object_Type):
        self.refcount = 1
        self.name = name
        self.type_obj = cl_type.CL_Type(type_obj)
        if name is None:
            self.dec_ref()

    def __repr__(self):
        return '<Object CL_Object {refcount: %s; name: %s; type: %s;}>' \
            %(self.refcount, self.name, self.type_obj)

    def inc_ref(self):
        '''Increment Reference (GC)'''
        self.refcount += 1

    def dec_ref(self):
        '''Decrement Reference (GC).'''
        self.refcount -= 1

    def CL_repr(self):
        return self.__repr__()
