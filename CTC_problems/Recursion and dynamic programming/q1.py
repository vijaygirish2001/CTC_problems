'''
Triple Step: A child is running up a staircase with n steps and
can hop either 1 step, 2 steps, or 3 steps at a time.
Implement a method to count how many possible ways the child can
run up the stairs.
'''

memo = dict()


# Count no of ways to run up the stairs
def count_ways(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        if n not in memo:
            memo[n] = count_ways(n-1) + count_ways(n-2) + count_ways(n-3)
        return memo[n]


# Print sample output for 19 steps
print(count_ways(19))
