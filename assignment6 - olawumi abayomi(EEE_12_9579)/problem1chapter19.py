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

def readposint():
    # The operation inside the while loop continues until a valid input is supplied
    while True:
        try:
            a = int(input("Please enter a positive integer: "))
            if a <= 0:
                print("Non-positive integers are not allowed")
            else:
                break
        except ValueError as e:
            print(e)


print("The positive integer you entered is", readposint())