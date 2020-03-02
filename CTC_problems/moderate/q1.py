

import numpy as np

def swap_no(a,b):
    a = a+b
    b = a-b
    a = a-b

    return a,b

a=1
b=-3
a,b =swap_no(a,b)

print(a,b)