s=input().split(',')
s2=""
for i in s:
    s1=i.split(':')
    n=len(s1[0])
    #n1=list(map(int,(s1[1])))
    while n>0:
        if str(n) in s1[1]:
            s2+=i[n-1]
            break
        n-=1
    else:
        s2+='x'
    
print(s2)
