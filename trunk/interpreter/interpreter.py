# ------------------------------------------------------------------
#
# run_clc.py:  Run the evaluator.  
# ------------------------------------------------------------------

import ply.yacc
import sys

import grammar
import interpreter_helper

def init_repl():
    '''Set things up before evaluation expressions.  This just mostly returns a
    dict of strings for configuration'''
    settings = {
            'ps1' : 'cl-calc #>'
        }
    return settings

def get_repl_exp():
    '''Get raw input from the keyboard.  This is meant to be fairly general and
    is basically just a wrapper keeping in mind that I may need to do more
    rigid error handling'''
    try:
        exp = raw_input()
    except EOFError:
        sys.exit(0)

    return exp

def eval_exp(exp):
    '''Evaluate single expression'''
    try:
        result = ply.yacc.parse(exp)
    except: 
        interpreter_helper.internal_error(exp, sys.exc_info()[0])
        # Uncomment for debugging
        #sys.excepthook(sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2])
        sys.exit(1)

    return result

def print_repl_prefix(prompt):
    '''Print the repl prefix.  This is another wrapper keeping in mind that I
    may need to expand this to allow different kinds of prompts'''
    print prompt,

def print_repl_result(result):
    '''Print the result of the evaluation of an expression.  This is another
    wrapper, but will soon be more encompassing.  I will need to do some
    serious type checking and coercion'''
    try:
        if result is None:
            return
        else:
            str_result = result.CL_repr()
    except:
        interpreter_helper.internal_error(result, sys.exc_info()[0])
        # Uncomment for debugging
        #sys.excepthook(sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2])
        sys.exit(1)

    print str_result


def eval_repl_exp():
    '''Put the interpreter together.  This gets and evaluates an expression
    from the keyboard.  Keep in mind that this does not include the loop, but
    just one expression'''
    repl_settings = init_repl()

    print_repl_prefix(repl_settings['ps1'])
    exp = get_repl_exp()
    result = eval_exp(exp)
    print_repl_result(result)

def run_repl():
    '''Run the repl.  This does nothing other than initiate a loop and call
    eval_repl_exp()'''
    while True:
        eval_repl_exp()

def get_interpreter(cls=None, filename=None):
    '''Stub for now.  Eventually I want the to be a dispatcher for the
    interpreter.  It should decide whether to interpret a file or from thre
    repl'''
    pass
