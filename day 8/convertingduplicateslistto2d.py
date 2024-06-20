n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
l1=[]
f=1
while(1):
        l3=[]
        for i in range(len(l)):
               if l[i]!='a' and l[i] not in l3:
                  l3.append(l[i])
                  l[i]='a'
        if not l3:
            break
        l1.append(l3)
print(l1)            
