# ------------------------------------------------------------------
#
# cl_decimal.py - Decimal type.  This basically replaces float in 
#                 the cl-calc language, although float is still 
#                 available.  This is just a wrapper around the 
#                 python type.
# ------------------------------------------------------------------


import decimal
import cl_object
import string_object

class CLDecimal(cl_object.CL_Object):
    '''CLDecimal is the default number type in the cl-calc language.  At this
    point it is the only one offered, but eventually int and float will be
    used.'''
    def __init__(self, val):
        self.decimal = decimal.Decimal(val) 
    
    # binary operators
    def __add__(self, other):
        return CLDecimal(self.decimal + to_cldecimal(other).decimal)
    
    def __sub__(self, other):
        return CLDecimal(self.decimal - to_cldecimal(other).decimal)

    def __mul__(self, other):
        return CLDecimal(self.decimal * to_cldecimal(other).decimal)

    def __div__(self, other):
        return CLDecimal(self.decimal / to_cldecimal(other).decimal)

    # comparison operators
    def __gt__(self, other):
        return CLDecimal(self.decimal > to_cldecimal(other).decimal)

    def __ge__(self, other):
        return CLDecimal(self.decimal >= to_cldecimal(other).decimal)

    def __lt__(self, other):
        return CLDecimal(self.decimal < to_cldecimal(other).decimal)

    def __le__(self, other):
        return CLDecimal(self.decimal <= to_cldecimal(other).decimal)

    def __eq__(self, other):
        return CLDecimal(self.decimal == to_cldecimal(other).decimal)

    def __neq__(self, other):
        return CLDecimal(self.decimal != to_cldecimal(other).decimal)

    def __nonzero__(self):
        return self.decimal != 0

    # string coercions
    def __repr__(self):
        # for debugging purposes, use the python obj('val') style
        return 'CLDecimal(\'%s\')' %(self.decimal)

    def CL_repr(self):
        # for use within the cl-calc language.  use a pure tostring style
        return '%s' %(self.decimal)

# convert numbers to decimals
def to_cldecimal(obj):
    '''Convert number to CLDecimal'''
    if isinstance(obj, CLDecimal):
        return obj
    if not isinstance(obj, float):
        return CLDecimal(obj)
    else:
        return CLDecimal(CL_String(obj))
