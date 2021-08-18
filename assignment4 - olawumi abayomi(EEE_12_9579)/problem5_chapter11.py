import sys
def test(status):
    lineno = sys._getframe(1).f_lineno
    if status == True:
        msg = 'Test at line {0} was OK '.format(lineno)
    else:
        msg = 'Test at line {0} Failed '.format(lineno)
    print(msg)



def add_vectors(u,v):
    # u = vector 1
    # v = vector 2
    new_vector = []
    for each_element in range(len(u)):
        new_element = u[each_element] + v[each_element]
        new_vector.append(new_element)
    return new_vector


def test_vector_adder():
    # Test
    test(add_vectors([1,1],[1,1])==[2,2])
    test(add_vectors([1,2],[1,4])==[2,6])
    test(add_vectors([1,2,1],[1,4,3])==[2,6,4])



test_vector_adder()