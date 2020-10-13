def solution(i):
    # Your code here
    n = 20250
    primeStr='23'
    for x in range(4,n+1):
        prime = True
        for y in range(2,int(x/2)+1):
            if x%y==0:
                prime=False
                break

        if prime:
            primeStr+=str(x)
        if len(primeStr)>i+4:
            break
    print(primeStr,'.')
    return primeStr[i:i+5]

print(solution(0))
print(solution(1))
print(solution(3))