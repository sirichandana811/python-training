n=int(input())
def prime(i,n):
       if n==1:
            return 0
       if i*i>n:
           return 1
       if n%i==0:
           return 0
       return prime(i+1,n)
def func(n,i):
    if i>n-i:
        return 0
    if prime(2,i)==1 and prime(2,n-i)==1:
        print(i,n-i)
        return 1
    return func(n,i+1)
print(func(n,1))
    
    
