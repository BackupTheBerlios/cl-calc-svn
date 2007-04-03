# ------------------------------------------------------------------------
# cl-lex.py
# 
# Tokenizer for the calculator evaluator.
# ------------------------------------------------------------------------

import ply.lex



# tokens
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'LBRACK',
    'RBRACK',
    'LBRACE',
    'RBRACE',
    'NEWLINE',
)


# token definitions
t_NUMBER = r'[0-9]*(\.)?[0-9]+'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'\/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACK = r'\['
t_RBRACK = r'\]'
t_LBRACE = r'\{'
t_RBRACE = r'\}'

def t_NEWLINE(t):
    r'\n'
    t.lexer.lineno += 1
    return t

# ignore these chars
t_ignore = ' \t'

# error definition
def t_error(t):
    print "Illegal character '%s'" %(t.value[0])
    t.lexer.skip(1)
    #Since PLY doesn't let me return my own types, I will have to
    #push my error onto the stack and then retrieve it
    #error.CLError(message='Illegal character "%s"' %(t.value[0]))

# set up lexer
ply.lex.lex()
