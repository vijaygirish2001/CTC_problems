'''


1. Output the maximum sum of a subtree in a binary tree.

   4   -> 11
 /  \
2   5

   4   -> 2
 /  \
2   5
     \
     -10


   4   -> 5
 /  \
2   5
     \
     -6
'''


class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right  = None

mx_sum = float('-inf')

def max_sum_subtree(n):
    global mx_sum
    if not n:
        return 0

    currsum = n.val + max_sum_subtree(n.left) + max_sum_subtree(n.right)

    mx_sum = max(currsum,mx_sum)



    return currsum


n = Node(4)

n.left = Node(2)
n.right = Node(5)
n.right.right = Node(-10)

max_sum_subtree(n)



print(mx_sum)