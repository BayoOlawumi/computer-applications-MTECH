#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Olawumi Abayomi
#
# Created:     20/07/2021
# Copyright:   (c) BayoOlawumi 2021
# Licence:     <your licence>

print("________________Question 5___________________")
# Calcuating the compound interest
# P represents the Principal Interest
p = 10000
# n represents the number of times the interest is compounded per year
n = 12
# t represents the number of years
t = input("Enter the number of years: ")
# Cast the imput to integer format
t = int(t)
# rate is represented as r, with the value 8%
r = 8/100
a = p * ((1 +(r/n)) ** (n*t))
print("The compound interest after {0} years is: {1}".format(t, a))














