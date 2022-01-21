def findSum(N):
    odd=0
    even=0
    
    while N>0:
        rem = N%10
        if(rem%2==0):
            even += rem
        else:
            odd += rem
        N //= 10
    
    li = [even,odd]
    return li

print(findSum(54321))