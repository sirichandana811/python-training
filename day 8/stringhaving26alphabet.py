s=input()
c=0
for i in range(len(s)):
    if s[i].isalpha() and  s[i] not in s[:i] :
        c=c+1
    if c==26:
        print("yes")
        break
else:
    print("no")
    
