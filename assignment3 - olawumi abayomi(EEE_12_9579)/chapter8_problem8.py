
import sys

def test(mirror):
    lineno = sys._getframe(1).f_lineno
    if mirror == True:
        msg = 'Test at line {0} was OK '.format(lineno)
    else:
        msg = 'Test at line {0} Failed '.format(lineno)
    print(msg)


# A function that mirrors its argument

def mirror(args):
    mirrored = str(args)
    each = -1
    while each >= -len(args):
        letter = args[each]
        # Append string from behind
        mirrored += letter
        each -= 1
    return mirrored

def test_suite():
    # Passed Test
    test(mirror("good")=='gooddoog')
    test(mirror("Python")=='PythonnohtyP')
    test(mirror("")=="")
    test(mirror("a")=="aa")


test_suite()