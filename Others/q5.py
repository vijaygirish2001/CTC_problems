'''
Write a function to return string when passed integer . Note : do not use tostring() in built function.

E.g 123 --> "123"

'''

def return_str(n):
    s= ''

    while n>0:
        s+= str(n%10)
        n= int(n/10)

    return s[-1::-1]

n= 1342
print(return_str(n))