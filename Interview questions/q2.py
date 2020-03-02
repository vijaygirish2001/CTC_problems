# Given a dictionary of words insert spaces at right places so that words are separated
import numpy as np
def insert_spaces(txt, dict_wrds, prev_txt = ''):
    if txt in dict_wrds:
        return prev_txt + ' ' + txt
    ind = 1
    fin_txt = None
    while ind <len(txt):
        if txt[:ind] in dict_wrds:
            fin_txt = insert_spaces(txt[ind:], dict_wrds,prev_txt + ' ' + txt[:ind])


        ind+=1
    if fin_txt:
        return fin_txt
    else:
        return prev_txt + ' ' + txt



dict_wrds =[ 'i','am','a', 'there', 'here' ]


a = insert_spaces('iamtherehh', dict_wrds)
print(a.strip())