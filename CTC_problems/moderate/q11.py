'''
Diving Board: You are building a diving board by placing a bunch of planks of wood end-to-end.
There are two types of planks, one of length shorter and one of length longer. You must use
exactly K planks of wood. Write a method to generate all possible lengths for the diving board
'''

pos_len = []
def possible_lengths(p,total, m,n, memo):
    global lengths

    if p == 0:

        lengths.append(total)
        return
    if str(total) + '-' + str(p) in memo:
        return

    possible_lengths(p-1, total+m, m,n, memo)
    possible_lengths(p - 1, total + n, m, n, memo)

    memo.append(str(total) + '-' + str(p))

    return

lengths = []

m=2
n =3
k=2
possible_lengths(k,0, m,n,  [])
print(set(lengths))

pos_len = []

for i in range(k+1):
    pos_len.append(m*i+n*(k-i))

print((pos_len))



