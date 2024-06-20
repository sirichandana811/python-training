s=input()
d={}
l=s.split(" ")
print(l)
d={}
l1=[0]*len(l)
for i in l:
    l1[int(i[-1])-1]=i[:len(i)-1]
print(" ".join(l1))
    
    
    
