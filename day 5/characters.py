key='hello world'
key=key.replace(' ','')
print(key)
s=''
for i in key:
    if i not in s:
        s=s+i
asc=97
for i in range(len(s)):
    
    s[i]=chr(asc)
    asc+=1
print(s)



s1=''
asc=97
for i in range(26):
    s1=s1+chr(asc) 
print(s1)
