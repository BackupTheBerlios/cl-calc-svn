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
import objects.string_object


# Precedence rules
#XXX == is binding tighter than +...need to fix
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('left', 'ASSIGN'),
    ('left', 'EQ', 'NE', 'LT', 'LE', 'GT', 'GE'),
)

AST = ast.CLAST()

# Grammar rules
def p_statement_expression(p):
    '''statement : expression'''
    p[0] = p[1]

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression EQ expression
                  | expression NE expression
                  | expression LT expression
                  | expression LE expression
                  | expression GT expression
                  | expression GE expression
                  | lvalue ASSIGN expression'''
    p[0] = AST.binop(p[1], p[3], p[2])

def p_expression_paren(p):
    '''expression : LPAREN expression RPAREN
                  | LBRACK expression RBRACK
                  | LBRACE expression RBRACE'''
    p[0] = p[2]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = objects.decimal_object.CLDecimal(p[1])

def p_expression_string(p):
    'expression : STRING'
    p[0] = objects.string_object.CL_String(p[1])

def p_expression_id(p):
    'expression : ID'
    p[0] = AST.lookup(p[1])

def p_lvalue_id(p):
    'lvalue : ID'
    p[0] = None


def p_err_expression(p):
    '''expression : expression error'''
    #XXX Todo: Add more sophisticated error handling
    print "Illegal expression."
    p[0] = None
    p.parser.error = 1

def p_error(p):
    pass

# Initialize parser
ply.yacc.yacc()
