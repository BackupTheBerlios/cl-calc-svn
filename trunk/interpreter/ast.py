# ------------------------------------------------------------
#
# ast.py - abstract syntax tree.  Defines a bunch of 
#             functions that evaluate an expression from
#             the context free grammar
#
# The reason that this is enclosed in a class is to encapsulate 
# the stack frame so that I can avoid globals.
# ------------------------------------------------------------

import sys
import os.path

import objects.cl_object
import lib.builtin

class CLAST(objects.cl_object.CL_Object):
    def binop(self, num1, num2, symbol):
        if symbol == '+':
            return lib.builtin.add(num1, num2)
        elif symbol == '-':
            return lib.builtin.subtract(num1, num2)
        elif symbol == '*':
            return lib.builtin.multiply(num1, num2)
        elif symbol == '/':
            return lib.builtin.divide(num1, num2)
        elif symbol == '=':
            return lib.builtin.assign(num1, num2)
