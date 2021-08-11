# A Program that sum all negative numbers in a list

# Given the following list as examples [-3,4,5,6,7,-9,1,2,3,-4,-6,7,9], [4,-6,5,1,-2,3,-4,5,-3,4,-3,5]

# function creation
def neg_num_summer(nums):
    initial_sum = 0
    for each_num in nums:
        # The conditional statement checks if number is less than 0.
        if each_num < 0:
            # add each number found guilty to the initial_sum
            initial_sum += each_num
    return initial_sum

# Program Execution with examples
list_one = [-3,4,5,6,7,-9,1,2,3,-4,-6,7,9]
list_two = [4,-6,5,1,-2,3,-4,5,-3,4,-3,5]

print("There sum of negative numbers in {1} is {0}".format(neg_num_summer(list_one),list_one))
print("There sum of negative numbers in {1} is {0}".format(neg_num_summer(list_two),list_two))