#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      BayoOlawumi
#
# Created:     13/09/2021
# Copyright:   (c) BayoOlawumi 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sys
def test(status):
    lineno = sys._getframe(1).f_lineno
    if status == True:
        msg = 'Test at line {0} was OK '.format(lineno)
    else:
        msg = 'Test at line {0} Failed '.format(lineno)
    print(msg)

def recursive_min(nxs):
    """
      Find the maximum in a recursive structure of lists
      within other lists.
      Precondition: No lists or sublists are empty.
    """
    smallest = None
    first_time = True
    for each_value in nxs:
        if type(each_value) == type([]):
            val = recursive_min(each_value)
        else:
            val = each_value

        if first_time or val < smallest:
            smallest = val
            first_time = False
    return smallest


test(recursive_min([2, 9, [1, 13], 8, 6]) == 1)
test(recursive_min([2, [[100, 1], 90], [10, 13], 8, 6]) == 1)
test(recursive_min([2, [[13, -7], 90], [1, 100], 8, 6]) == -7)
test(recursive_min([[[-13, 7], 90], 2, [1, 100], 8, 6]) == -13)