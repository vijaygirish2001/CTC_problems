def solution(x):
    a_uni = ord('a')
    z_uni = ord('z')

    mp = {}

    all_uni = list(range(a_uni,z_uni+1))
    all_uni = all_uni[::-1]

    ind = 0
    for i in range(a_uni,z_uni+1):
        mp[chr(i)] = chr(all_uni[ind])
        ind += 1

    y=''

    for i in x:
        if i in mp:
            y = y + mp[i]
        else:
            y= y + i



    return  y

x  = "wrw blf hvv ozhg mrtsg'h vkrhlwv?"
y = solution(x)
