

def isprime(n):
    if n in [2,3,5,7]:
        return 1
    return 0
def sum1(n):
  while n>=10:
     s=0
     while n>0:
      s=s*10+n%10
      n=n//10
     n=s
  print(n)
  return n
def fun(n):  
   n=sum1(n)
   if isprime(n)==1:
           return 0
   if isprime(n)==0:
           return 1
n=int(input())
while True:
    p=fun(n)
    if p==0:
        break
    n+=1
print(n)


        
