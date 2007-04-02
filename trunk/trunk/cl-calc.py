# ------------------------------------------------------------------
# 
# cl-calc.py - The main program for cl-calc. Parses command line
#              args and then dispatches to interpreter/interpreter.py
# ------------------------------------------------------------------

from optparse import OptionParser

from interpreter import interpreter

def parse_options():
    '''Get cmd line options'''
    parser = OptionParser()
    (options, args) = parser.parse_args()
    return (options, args)

if __name__ == '__main__':
    (options, args) = parse_options()
    interpreter.run_repl()
