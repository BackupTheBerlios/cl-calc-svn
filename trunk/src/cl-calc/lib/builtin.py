# ------------------------------------------------------------------
#
# cl_builtins.py - Built in functions
# ------------------------------------------------------------------

import objects.true_object
import objects.false_object

def add(obj1, obj2):
    return obj1 + obj2

def subtract(obj1, obj2):
    return obj1 - obj2

def multiply(obj1, obj2):
    return obj1 * obj2

def divide(obj1, obj2):
    return obj1 / obj2

def equal(obj1, obj2):
    return boolean(obj1 == obj2)

def nequal(obj1, obj2):
    return boolean(obj1 != obj2)

def greater(obj1, obj2):
    return boolean(obj1 > obj2)

def greater_equal(obj1, obj2):
    return boolean(obj1 >= obj2)

def less(obj1, obj2):
    return boolean(obj1 < obj2)

def less_equal(obj1, obj2):
    return boolean(obj1 <= obj2)

def boolean(predicate):
    if predicate:
        return objects.true_object.CL_True()
    else:
        return objects.false_object.CL_False()

def assign(symtable, name, val):
    pass

def lookup(symtable, name):
    pass
