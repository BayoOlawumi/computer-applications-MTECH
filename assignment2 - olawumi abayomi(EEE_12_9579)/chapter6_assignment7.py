import sys

# The function that does the conversion
def to_secs(hour, min, sec):
    hours_sec = hour * 60 * 60
    min_sec = min * 60
    return hours_sec + min_sec + sec

def test(to_secs):
    lineno = sys._getframe(1).f_lineno
    if to_secs == True:
        msg = 'Test at line {0} was OK '.format(lineno)
    else:
        msg = 'Test at line {0} Failed '.format(lineno)
    print(msg)

def test_sec():
    test(to_secs(2,30,10)==9010)
    test(to_secs(2,0,0)==7200)
    test(to_secs(0,2,0)==120)
    test(to_secs(0,0,42)==42)
    test(to_secs(0,-10,10)==-590)

test_sec()
