n=int(input())
def func(n,s):
    if n>0:
        return func(n//10,s*10+n%10)
    else:
        return s
if func(n,0)==n:
    print("true")
else:
    print("false")
