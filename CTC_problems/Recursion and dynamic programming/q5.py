'''
 Recursive Multiply: Write a recursive function to multiply two positive integers without using
the * operator (or / operator). You can use addition, subtraction, and bit shifting, but you should
minimize the number of those operations
'''

def rec_multiply(a,b):

    if a>b:
        min_val = b
        max_val = a
    else:
        min_val = a
        max_val = b



    def divide_multiply(min_val, max_val):
        if min_val == 0:
            return 0
        if min_val == 1:
            return max_val

        mval = min_val>>1
        p= divide_multiply(mval, max_val)


        if min_val%2 ==0:
            return p+p
        else:
            return p+p+max_val

    return divide_multiply(min_val, max_val)

print(rec_multiply(35,30))