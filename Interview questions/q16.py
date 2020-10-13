T = int(input())

for i in range(T):
    K = int(input())
    A = [int(j) for j in input().split()]

    no_rules_brk = 0

    ind = 1
    while ind < len(A):
        no_seq = 1
        while ind < len(A) and A[ind] >= A[ind - 1]:
            if A[ind] > A[ind - 1]:
                no_seq += 1
            ind += 1
        if no_seq > 4:
            no_rules_brk += (no_seq - 1) // 4

        no_seq = 1
        while ind < len(A) and A[ind] <= A[ind - 1]:
            print(A[ind], A[ind-1])
            if A[ind] < A[ind - 1]:
                no_seq += 1
            ind += 1
        print(no_seq)
        if no_seq > 4:
            no_rules_brk += (no_seq - 1) // 4

    print('Case #' + str(i + 1) + ': ' + str(no_rules_brk))
