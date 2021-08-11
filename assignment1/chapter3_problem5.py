print("---------------------Question 5a- A loop that prints each of the numbers on a new line-----------------")
xs = [12,10,32,3,66,17,42,99,20]
# A loop that prints each of the numbers on a new line
for each in xs:
    print(each)


print("---------------------Question 5b-A loop that prints each number and its square on a new line-----------------")
# A loop that prints each number and its square on a new line
for each in xs:
    print(each, "---", each**2)


print("---------------------Question 5c-A loop that add all the number in the list into a variable called total-----------------")
# A loop that add all the number in the list into a variable called total
total = 0
for each in xs:
    total+=each
print("The sum of all the number in the list is : ", total)


print("---------------------Question 5d-Print Product of all numbers in the list-----------------")
# A loop that add all the number in the list into a variable called total
prd = 1
for each in xs:
    prd*=each
print("The product of all the number in the list is : ", prd)
