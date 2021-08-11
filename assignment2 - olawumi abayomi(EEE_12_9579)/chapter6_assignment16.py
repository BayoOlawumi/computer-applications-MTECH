import sys

# The function that does the factor checking
def is_factor(f, n):
    # Check if there is no remainder on division
    if n % f ==0:
        return True
    else:
        return False

def test(is_factor):
    lineno = sys._getframe(1).f_lineno
    if is_factor == True:
        msg = 'Test at line {0} was OK '.format(lineno)
    else:
        msg = 'Test at line {0} Failed '.format(lineno)
    print(msg)

def test_suite():
    test(is_factor(3, 12))
    test(not is_factor(5, 12))
    test(is_factor(7, 14))
    test(not is_factor(7, 15))
    test(is_factor(1, 15))
    test(is_factor(15, 15))
    test(not is_factor(2, 15))

test_suite()
