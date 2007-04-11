# ------------------------------------------------------------------
#
# type.py - The type cl_object.
# ------------------------------------------------------------------

# Dummy type classes for types to avoid the use of string comparison

class Error_Type:
    pass

class Object_Type:
    pass

class Number_Type:
    pass

class String_Type:
    pass

class List_Type:
    pass

class Dict_Type:
    pass
 
class CL_Type(object):
    def __init__(self, obj_type=Object_Type):
        self.type = obj_type

    def __repr__(self):
        if self.type == Error_Type:
            return 'Error'
        elif self.type == Object_Type:
            return 'Object'
        elif self.type == Number_Type:
            return 'Number'
        elif self.type == String_Type:
            return 'String'
        elif self.type == List_Type:
            return 'List'
        elif self.type == Dict_Type:
            return 'Dict'

    def check_type(self, obj_type):
        if not (obj_type == Error_Type \
               or obj_type == Object_Type \
               or obj_type == Number_Type \
               or obj_type == String_Type \
               or obj_type == List_Type \
               or obj_type == Dict_Type):
            # XXX
            # Todo: Create an error if none of these types are used
            pass
