# A neat multiplication table

for a in range(13):
    if a > 0:
        if len(str(a)) >1:
            print(str(a) + ": ", end=" ")
        else:
            print(str(a) + ": ", end="  ")
    else:
        print("    ", end=" ")
    for b in range(1,13):
        if a == 0:
            if len(str(b)) >1:
                print(b, end=" ")
            else:
                print(b, end="  ")
        elif a >=1:
            multipl = str(a*b)
            if len(multipl) >1:
                print(multipl, end=" ")
            else:
                print(multipl, end="  ")
    print()