
# @return a list of list of integers
def subsetsWithDup(A):

    all_subsets = []
    res = []

    def subset(result, cur, rest):
        if not rest:
            #if cur not in result:
            result += [cur]
        else:
            subset(result, cur, rest[1:])
            subset(result, cur + [rest[0]], rest[1:])

    subset(res, [], sorted(A))

    return sorted(res)

def subsets( A):
    res = []

    def recur_subs(res, s, left):
        if not left:

            res += [s]
            return
        print(left)
        recur_subs(res, s + [left[0]], left[1:])
        recur_subs(res, s, left[1:])

    print(A)
    recur_subs(res, [], A)

    return res


print(subsets([1,2,3]))