import sys
def test(count):
    lineno = sys._getframe(1).f_lineno
    if count == True:
        msg = 'Test at line {0} was OK '.format(lineno)
    else:
        msg = 'Test at line {0} Failed '.format(lineno)
    print(msg)
def counter(sub, totalstring):
    count = 0
    start  = 0
    while start < len(totalstring):
        pos = totalstring.find(sub, start)
        if pos != -1:
            start = pos + 1
            count += 1
        else:
            break
    return count

def test_counter():
    # Passed Test
    test(counter("is", "Mississippi")==2)
    test(counter("an","banana")==2)
    test(counter("ana","banana")==2)
    test(counter("nana","banana")==1)
    test(counter("nanan","banana")==0)
    test(counter("aaa","aaaaaa") ==4 )


test_counter()