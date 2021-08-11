import sys

# The function that does the celsius to farenheint  conversion
def c2f(cel):
    farh = (cel * (9/5)) + 32
    return round(farh)

def test(c2f):
    lineno = sys._getframe(1).f_lineno
    if c2f == True:
        msg = 'Test at line {0} was OK '.format(lineno)
    else:
        msg = 'Test at line {0} Failed '.format(lineno)
    print(msg)

def test_suite():
    test(c2f(0) == 32)
    test(c2f(100) == 212)
    test(c2f(-40) == -40)
    test(c2f(12) == 54)
    test(c2f(18) == 64)
    test(c2f(-48) == -54)

test_suite()
