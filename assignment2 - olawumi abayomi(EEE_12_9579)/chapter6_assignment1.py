import sys

def test_next(turn_clockwise_fn):
    lineno = sys._getframe(1).f_lineno
    if turn_clockwise_fn == True:
        msg = 'Test at line {0} was OK '.format(lineno)
    else:
        msg = 'Test at line {0} Failed '.format(lineno)
    print(msg)



compass_points = ['N','E','S','W']

def turn_clockwise(point):
    # change lowercase to uppercase
    point = str(point).upper().strip()
    # remove spaces and check if the supplied point is valid
    if point in compass_points:
        location = compass_points.index(point)
        if location == 3:
            return compass_points[0]
        else:
            return compass_points[location+1]
    else:
        return None

def test_suite():
    # Passed Test
    test_next(turn_clockwise("N")=='E')
    test_next(turn_clockwise("W")=='N')
    test_next(turn_clockwise(42)==None)
    test_next(turn_clockwise("rubbish")==None)


test_suite()