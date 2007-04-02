# ------------------------------------------------------------------
#
# cl_yacc.py - The main parser module.  Works closely with cl_lex.py
#              where all tokens are defined.
# ------------------------------------------------------------------

import ply.yacc
import sys
import os

from token import tokens

import ast
import objects.decimal_object


# Precedence rules
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('left', 'ASSIGN'),
)

AST = ast.CLAST()

# Grammar rules
def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    p[0] = AST.binop(p[1], p[3], p[2])

def p_expression_paren(p):
    '''expression : LPAREN expression RPAREN
                  | LBRACK expression RBRACK
                  | LBRACE expression RBRACE'''
    p[0] = p[2]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = objects.decimal_object.CLDecimal(p[1])

def p_error(p):
    print "Syntax error on input"
    while 1:
        token = ply.yacc.token()
        if token is None:
            break
    ply.yacc.restart()
    return

# Initialize parser
ply.yacc.yacc()
