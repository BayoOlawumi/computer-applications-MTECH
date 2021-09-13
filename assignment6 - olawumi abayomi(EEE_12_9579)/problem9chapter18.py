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

import sys, time


def recursion_depth(a):
    recursion_depth(int(a))


print(sys.getrecursionlimit())
sys.setrecursionlimit(5000)
print(sys.getrecursionlimit())
time.sleep(2)
recursion_depth(1)
