import sys
def test(status):
    lineno = sys._getframe(1).f_lineno
    if status == True:
        msg = 'Test at line {0} was OK '.format(lineno)
    else:
        msg = 'Test at line {0} Failed '.format(lineno)
    print(msg)



def dot_product(vector1,vector2):
    # Initialize an empty varaible
    scalar_result = 0
    for each_element in range(len(vector1)):
        multiplied =  vector1[each_element] * vector2[each_element]
        # Add multiplied to the previous sum on every iteration
        scalar_result = scalar_result + multiplied
    #return dot_product answer
    return scalar_result


def test_scalar_mulitplication():
    # Test
    test(dot_product([1,1],[1,1])==2)
    test(dot_product([1,2],[1,4])==9)
    test(dot_product([1,2,1],[1,4,3])==12)



test_scalar_mulitplication()