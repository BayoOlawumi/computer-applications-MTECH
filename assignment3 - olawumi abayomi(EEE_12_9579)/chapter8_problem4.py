def counter(my_string, my_letter, given_position):
    count = 0
    for each_letter in my_string[given_position:]:
        if each_letter == my_letter:
            count+=1
    return count

str_given = input("Enter a string: ")
letter_given = input("Enter the letter you want to count: ")
position_given = int(input("Enter the starting position: "))
count = counter(str_given,letter_given, position_given)
print("{0} appeared {1} times".format(str_given,count))



