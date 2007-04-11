# ------------------------------------------------------------------
#
# interpreter_helpyer.py - convenience functions for the interpreter
# ------------------------------------------------------------------

def internal_error(expr, expn, msg=None):
    print "Internal error occurred while evaluating expression: %s (%s)" \
            %(expr, expn)

    if msg is not None:
        print msg
