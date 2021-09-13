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

def flatten(s):
    extracted_list = []
    for each_element in s:
        # Checks if incoming element is a list
        if type(each_element) == list or type(each_element) == tuple:
            extracted_list.extend(flatten(each_element))
        else:
            # add to existing element
            extracted_list.append(each_element)
    return extracted_list


test(flatten([2, 9, [2, 1, 13, 2], 8, [2, 6]]) == [2, 9, 2, 1, 13, 2, 8, 2, 6])
test(flatten([[9, [7, 1, 13, 2], 8], [7, 6]]) == [9, 7, 1, 13, 2, 8, 7, 6])
test(flatten([[9, [7, 1, 13, 2], 8], [2, 6]]) == [9, 7, 1, 13, 2, 8, 2, 6])
test(flatten([["this", ["a", ["thing"], "a"], "is"], ["a", "easy"]]) ==
     ["this", "a", "thing", "a", "is", "a", "easy"])
test(flatten([]) == [])