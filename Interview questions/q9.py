def solution(x):
    ind = 0
    while ind < len(x):
        temp = x[ind].split('.')
        temp =[int(i) for i in temp]
        ext = 3 - len(temp)
        if ext:
            temp = temp + [-1]*ext

        x[ind] = temp
        ind += 1
    x = sorted(x)
    y= []
    for i in x:
        temp = []
        for j in i:
            if j == -1:
                break
            temp.append(j)
        temp = [str(i) for i in temp]
        y.append(temp)
    y = ['.'.join(i) for i in y ]
    return y

x= ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]

y = solution(x)

print(y)



