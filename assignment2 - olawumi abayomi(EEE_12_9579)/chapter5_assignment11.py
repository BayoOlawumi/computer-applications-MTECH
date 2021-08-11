# Import the math library
import math

def right_angled(l1,l2,l3):
    calculated = math.sqrt(l1**2 + l2**2)
    if abs(l3 - calculated) <= 0.000001:
        return True
    else:
        return False

# EXAMPLE
l1 = 3
l2 = 4
l3 = 5
print(right_angled(l1,l2,l3))