'''


Giving a the following:

A list of a store items T={t_1, t_2,...,t_n}.

A list of prices of each item P={p_1, p_2,...,p_n}.

A list of quantities of each item Q={q_1, q_2,...,q_n}, respectively.

And total bill M.

Our goal is to find any possible list of items that its total value is equal to M using dynamic problem.

Write down a recursive solution.

- xi.text.xi 5 months ago in United States for n
'''


def possible_list(T,P,Q,M):
    tot_item = []
    for i in range(0,len(P)):
        item = P[i]*Q[i]
        if item == M :
            return [T[i]]
        tot_item.append(item)

    seen_dict = dict()
    def sub_list(tot_item, ind, sm, seen_dict):
        if ind>=len(tot_item):
            if sm==0:
                return 1
            else:
                return 0
        if (ind, sm) not in seen_dict:
            count = sub_list(tot_item,ind+1, sm, seen_dict)
            count += sub_list(tot_item,ind+1, sm -tot_item[ind], seen_dict)
            seen_dict[(ind,sm)]= count
        return seen_dict[(ind, sm)]


    def extract_lst(tot_item, sm, seen_dict):
        fin_lst = []
        for j in range(len(tot_item)):
            if sub_list(tot_item, j+1,sm -tot_item[j], seen_dict ):
                fin_lst.append(tot_item[j])
                sm -= tot_item[j]
        return fin_lst


    fin_cnt = sub_list(tot_item,0,M,seen_dict)
    fin_lst = extract_lst(tot_item, M, seen_dict)



    return fin_cnt, fin_lst

T = ['s','d','g']
P = [1,4,2,9]
Q = [1,1,1,1]
M = 5
fin_cnt, fin_lst = possible_list(T,P,Q,M)

print(fin_cnt, fin_lst)

