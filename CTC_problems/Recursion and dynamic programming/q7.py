'''
8.7 Permutations without Dups: Write a method to compute all permutations of a string of unique
characters.
'''

def perms_str(a, ind):
    if ind == 0:
        return [a[:1]]
    prev_str_list = perms_str(a, ind - 1)
    all_str = []
    print(prev_str_list)
    for prev_str in prev_str_list:
        for k, i in enumerate(prev_str):
            all_str.append(prev_str[:k]+ a[ind]+prev_str[k:])

        all_str.append(prev_str+a[ind])

    return  all_str

a='cnt'
print(perms_str(a, len(a)-1))