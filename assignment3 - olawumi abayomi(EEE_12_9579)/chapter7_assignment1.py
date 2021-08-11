# A function that count the number of odd numbers in a list

# Given the following list as examples [3,4,5,6,7,8,9,1,2,3,4,4,6,7,9], [34,56,65,21,2,3,4,5,3,4,23,5]

# function creation
def odd_num_counter(nums):
    count = 0
    for each_num in nums:
        # The conditional statement checks if a remainder exists on dividing each of the number by 2.
        if each_num % 2 !=0:
            # increment the variable count by 1 if condition is True
            count = count+1
    return count

# Program Execution
list_one = [3,4,5,6,7,8,9,1,2,3,4,4,6,7,9]
list_two = [34,56,65,21,2,3,4,5,3,4,23,5]

print("There are {0} odd numbers in {1}".format(odd_num_counter(list_one),list_one))
print("There are {0} odd numbers in {1}".format(odd_num_counter(list_two),list_two))