'''

A bracket is considered to be any one of the following characters: (, ), {, }, [, or ].

Two brackets are considered to be a matched pair if the an opening bracket (i.e., (, [, or {) occurs to the left of a closing bracket (i.e., ), ], or }) of the exact same type. There are three types of matched pairs of brackets: [], {}, and ().

A matching pair of brackets is not balanced if the set of brackets it encloses are not matched. For example, {[(])} is not balanced because the contents in between { and } are not balanced. The pair of square brackets encloses a single, unbalanced opening bracket, (, and the pair of parentheses encloses a single, unbalanced closing square bracket, ].

By this logic, we say a sequence of brackets is balanced if the following conditions are met:

It contains no unmatched brackets.
The subset of brackets enclosed within the confines of a matched pair of brackets is also a matched pair of brackets.
Given  strings of brackets, determine whether each sequence of brackets is balanced. If a string is balanced, return YES. Otherwise, return NO.
'''


def isBalanced(s):
    start_close = dict()
    start_close['('] = ')'
    start_close['['] = ']'
    start_close['{'] = '}'

    arr = []
    for i in s:
        if i in start_close:
            arr.append(i)
        else:
            if arr and start_close[arr.pop(-1)] == i :
                pass
            else:
                return 'NO'
    if not arr:
        return 'YES'
    return 'NO'



print(isBalanced('[{}]'))


def icecreamParlor(m, arr):
    dict_comp = dict()
    ind = 0
    while ind< len(arr):
        dict_comp[ind] = m- arr[ind]
        ind+=1
    valid_ind = []
    ind = 0
    while ind< len(arr):


    return valid_ind

m = 4
arr = [2,2,4,3]

v = icecreamParlor(m, arr)
