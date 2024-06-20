n=int(input())
def func(n):
    if n==0:
        return 0
    return n+func(n-2)
if n%2!=0:
    n-=1
print(func(n))
