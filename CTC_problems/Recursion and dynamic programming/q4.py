'''
Power Set: Write a method to return all subsets of a set.
'''

def allsublist(a):
    if a ==[]:
        return [[]]
    x= allsublist(a[1:])
    print(x)

    return x + [[a[0]] +y for y in x]

print(allsublist([1,4,6,2]))