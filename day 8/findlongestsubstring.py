s=input()
i1=0
j1=1
m=0
d={}
d[s[0]]=0
while j1<len(s):
    if s[j1] in s[i1:j1]:
        i1=d[s[j1]]+1
    d[s[j1]]=j1
    j1+=1
    m=max(m,j1-i1)
print(m)   
    
