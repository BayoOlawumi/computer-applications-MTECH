#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      BayoOlawumi
#
# Created:     13/09/2021
# Copyright:   (c) BayoOlawumi 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

words = input("Enter any sentence").lower()

alphabet = 'abcdefghijklmnopqrstuvwxyz'

letter_count = {} # empty dictionary
for each_char in words:
    if each_char in alphabet:
        if each_char in letter_count:
            # check if each_char already exist in the dictionary and get the last count number
            letter_count[each_char] = letter_count[each_char] + 1
        else:
            letter_count[each_char] = 1

keys = letter_count.keys()

for char in sorted(keys):
    print(char, letter_count[char])