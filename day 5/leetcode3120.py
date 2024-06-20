word="aaAbcBC"
c=0
l=""
s=""
for i in word:
            if i.isupper() and i.lower() in word and i not in s:
                   c+=1
                   s+=i
print(c)
