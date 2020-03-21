'''
Problem:
1. Given a Mix of all types of characters which includes Special characters, Numbers, String in a Log file.
for eg: "HappyI%&&87Christmas %%$^%&NewYear"
2. Get the largest substring which
"contains the Characters in Even Position followed by a Special Character and
then a meaningful word should be coming up"
'''

import re
def largest_substr(txt):
    txt = re.sub('[^a-zA-Z]',' ',txt)
    txt_lst = txt.split(' ')
    l=0
    mx_str = txt
    for t in txt_lst:

        if len(t)> l:
            mx_str = t
            l = len(t)

    return mx_str


print(largest_substr('dsdsd;;ere'))