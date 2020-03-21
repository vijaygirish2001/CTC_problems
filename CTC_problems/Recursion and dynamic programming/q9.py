'''
Parens: Implement an algorithm to print all valid (i.e., properly opened and closed) combinations
of n pairs of parentheses.
EXAMPLE
Input: 3
Output: (( () ) ) , ( () () ) , ( () ) () , () ( () ) , () () ()
'''

def valid_paran(leftrem,rightrem,pairs,s):
    if leftrem==0 and rightrem == 0:
        pairs.append(s)

    if rightrem<leftrem or leftrem<0:
        return

    valid_paran(leftrem-1, rightrem, pairs, s+'(')

    valid_paran(leftrem, rightrem-1, pairs, s + ')')


n=4
leftrem = n
rightrem = n
pairs = []
valid_paran(leftrem,rightrem,pairs,'')

print(pairs)