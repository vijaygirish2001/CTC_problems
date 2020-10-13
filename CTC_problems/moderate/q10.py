'''
16.10 Living People: Given a list of people with their birth and death years, implement a method to
compute the year with the most number of people alive. You may assume that all people were born
between 1900 and 2000 (inclusive). If a person was alive during any portion of that year, they should
be included in that year's count. For example, Person (birth= 1908, death= 1909) is included in the
counts for both 1908 and 1909.
'''

from collections import defaultdict

def max_living(date_list):
    no_ppl = defaultdict(int)

    for i in date_list:
        no_ppl[i[0]] += 1

        no_ppl[i[1]+1]  -=1

    yrs = no_ppl.keys()
    max_alive =0
    curr_alive =0
    for i in range(min(no_ppl.keys()),max(no_ppl.keys())+1):
        if i in no_ppl:
            curr_alive += no_ppl[i]
        if max_alive< curr_alive:
            max_alive = curr_alive

    return max_alive


dates = [ [12,15], [20,90], [10,98], [1,72], [10,98], [23,82], [13,98], [90,98], [83,99] ,[75,94]]
print(max_living(dates))
