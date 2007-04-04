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

import lib.builtin
import objects.cl_object
import symbol_table

class CLAST(objects.cl_object.CL_Object):
    def __init__(self):
        self.symtable = symbol_table.SymbolTable()

    #XXX num1 and num2 are bad names - can be any type of object
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
            return lib.builtin.assign(self.symtable, num1, num2)
        elif symbol == '==':
            return lib.builtin.equal(num1, num2)
        elif symbol == '!=':
            return lib.builtin.nequal(num1, num2)
        elif symbol == '<':
            return lib.builtin.less(num1, num2)
        elif symbol == '<=':
            return lib.builtin.less_equal(num1, num2)
        elif symbol == '>':
            return lib.builtin.greater(num1, num2)
        elif symbol == '>=':
            return lib.builtin.greater_equal(num1, num2)

    def lookup(self, symbol, value):
        return lib.builtin.lookup(symbol)
