# ------------------------------------------------------------------
#
# object_reference.py - Keep track of object references in the 
#                       symbol table
# ------------------------------------------------------------------

import objects.cl_object

class ObjectReference(objects.cl_object.CL_Object):
    def __init__(self, name=None, obj_val=None):
        self. name = name
        self.obj_val = obj_val
        self.ref_count = 1

    def inc_ref(self):
        self.ref_count += 1

    def dec_ref(self):
        self.ref_count -= 1
