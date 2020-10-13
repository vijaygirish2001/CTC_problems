'''
Write a function given a string return all nearby words
'''

near_by_char= {'i':['e','a'], 's':['t','m']}

valid_wrds = ['is','es','it','at']



def nearby_wrds(s, new_wrd, index, all_wrds):
    if index == len(s) :
        if new_wrd in valid_wrds:
            all_wrds.append(new_wrd)

        return all_wrds

    all_wrds = nearby_wrds(s, new_wrd + s[index], index+1, all_wrds)
    if near_by_char.get(s[index]):
        for i in near_by_char[s[index]]:
            all_wrds= nearby_wrds(s, new_wrd + i, index+1, all_wrds)

    return all_wrds


all_wrds = nearby_wrds('is','',0,[])

print(all_wrds)


def find_pivot(strt, end, A):
    mid = (strt + end) // 2
    print(strt, end, mid)
    if A[mid] > A[mid + 1]:
        return A[mid + 1]
    if A[mid] < A[mid - 1]:
        return A[mid]
    if A[strt] > A[mid]:
        m= find_pivot(strt, mid - 1, A)
    else:
        print(strt, end, A[strt], A[mid])
        m = find_pivot(mid + 1, end, A)

    return m

A= [ 40342, 40766, 41307, 42639, 42777, 46079, 47038, 47923, 48064, 48083, 49760, 49871, 51000, 51035, 53186, 53499, 53895, 59118, 60467, 60498, 60764, 65158, 65838, 65885, 65919, 66638, 66807, 66989, 67114, 68119, 68146, 68584, 69494, 70914, 72312, 72432, 74536, 77038, 77720, 78590, 78769, 78894, 80169, 81717, 81760, 82124, 82583, 82620, 82877, 83131, 84932, 85050, 85358, 89896, 90991, 91348, 91376, 92786, 93626, 93688, 94972, 95064, 96240, 96308, 96755, 97197, 97243, 98049, 98407, 98998, 99785, 350, 2563, 3075, 3161, 3519, 4176, 4371, 5885, 6054, 6495, 7218, 7734, 9235, 11899, 13070, 14002, 16258, 16309, 16461, 17338, 19141, 19526, 21256, 21507, 21945, 22753, 25029, 25524, 27311, 27609, 28217, 30854, 32721, 33184, 34190, 35040, 35753, 36144, 37342 ]

m = find_pivot(0, len(A)-1, A)