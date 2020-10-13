
def prevSmaller( array):
    """ Time complexity: O(n). Space complexity: O(n), n is len(array).
    """
    stack = []
    result = []
    for num in array:
        print(num, stack)
        # see of there's integer smaller than num in the stack
        while stack and stack[-1] >= num:
            stack.pop()
        if stack:  # found the smaller integer
            result.append(stack[-1])
        else:  # stack is empty, smaller integer wasn't found
            result.append(-1)
        stack.append(num)  # push current num to the stack
    return result

print(prevSmaller([1, 4, 5, 2, 2, 8]))


def solve( A):
    st = []
    st_seen = []
    b = ''
    for ind,i in enumerate(A):

        if i not in A[:ind]:
            st.append(i)
        elif i in st:
            st.remove(i)
        print(st,i)
        if st:
            b += st[0]
        else:
            b += '#'

    return b

print(solve('jpxvxivxkkthvpqhhhjuzhkegnzqriokhsgea'))


def solve( A):
    ind = 0
    s = len(A)
    k = 0
    while ind <= int(len(A) / 2)+1:
        print(A[ind], A[s - ind - 1])
        if A[ind] != A[s - ind - 1]:
            B = A[:ind] + A[ind + 1:]
            C = A[:s - ind - 1] + A[s - ind:]
            if B == B[::-1] or C == C[::-1]:
                return 1

        ind += 1

    if len(A) % 2 == 1:
        B = A[:int(len(A) / 2)] + A[int(len(A) / 2) + 1:]
        print(B)
        if B == B[::-1]:
            return 1

    return 0


print(solve("epyyevdadveyype"))