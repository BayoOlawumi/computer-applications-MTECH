import sys
def test(status):
    lineno = sys._getframe(1).f_lineno
    if status == True:
        msg = 'Test at line {0} was OK '.format(lineno)
    else:
        msg = 'Test at line {0} Failed '.format(lineno)
    print(msg)



def scalar_multi(scalar,vector):
    # Initialize an empty list
    new_vector = []
    for each_element in range(len(vector)):
        new_element =  scalar * vector[each_element]
        # Add element to the new list after multiplication
        new_vector.append(new_element)
    #return created vector
    return new_vector


def test_scalar_mulitplication():
    # Test
    test(scalar_multi(5,[1,2])==[5,10])
    test(scalar_multi(3,[1,0,-1])==[3,0,-3])
    test(scalar_multi(7,[3,0,5,11,2])==[21,0,35,77,14])



test_scalar_mulitplication()