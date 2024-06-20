s1="tu5g7k1h8"
s2="g5g8gd6h3"
l=[]
for i in s1:
    if i.isdigit():
        l.append(i)
for i in s2:
    if i.isdigit() and i not in l:
        l.append(i)
l.sort(reverse=True)
print(l)
for i in range(len(l)-1,-1,-1):
    if int(l[i])%2==0:
        '''n=l[i]
        while i<len(l)-1:
            l[i]=l[i+1]
            i+=1
        l[-1]=n'''
        l.append(l.pop(i))
        print("".join(l))
        break
else:
    print(-1)
