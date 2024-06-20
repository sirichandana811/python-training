n=int(input())
l=[]
for i in range(n):
     l1=[]
     for j in range(n):
         l1.append(input())
     l.append(l1)
s=input()
f=1
for i in range(len(s)):
    if s[i] not in l[i%n]:
        f=0
        break
    else:
        l[i%n].remove(s[i])
print(l)
if f==0:
    print("no")
else:
    print("yes")
    

        
    


