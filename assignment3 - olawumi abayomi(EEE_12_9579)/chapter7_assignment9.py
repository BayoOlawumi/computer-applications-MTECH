
def triangular_numbers(n):
    num = 0
    triangulars = []
    for n in range(n):
         num += 1
         tri_num = round((num*(num+1))/2)
         triangulars.append(tri_num)
    return triangulars


def program(n):
    tris = triangular_numbers(n)
    count= 0
    for tri in tris :
        count = count+1
        print(count, end = " ")
        print(tri, end = " ")
        print()



#  n = 5
program(5)
