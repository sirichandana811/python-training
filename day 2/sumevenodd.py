l=[0,0]
a=[3,8,5,4,3]
b=[5,0,9,3,2]
def func(x,s1,s2):
    if x==len(a):
        return s1,s2
    if a[x]%2==0:
        s1+=a[x]
    if b[x]%2!=0:
        s2+=b[x]
    return func(x+1,s1,s2)
print(func(0,0,0))
    
