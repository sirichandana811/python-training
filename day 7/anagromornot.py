s=input()
n=int(input())
l=[]
l1=[]
for i in range(n):
    l1=[]
    l1.append(input())
    l1.append(int(input()))
    l.append(l1)
s1=""
l2=[]
for i in l:
    if i[0]=="l":
        l2.append(s[i[1]])
    else:
        l2.append(s[-i[1]])
s1="".join(sorted(l2))
print(s1)
l3=[]
i=0
while i<len(s)-(n+1):
    if s1=="".join(sorted(s[i:i+len(s1)])):
        print("yes")
        break
    i+=1
        
else:
        print("no")



    
        
        
    


