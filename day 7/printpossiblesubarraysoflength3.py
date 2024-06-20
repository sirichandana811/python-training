n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))

def func(l,l2,i,n):
    l1=[]
    if len(l2)==3:
        print(l2)
        return
    for j in range(i,n):
        l2.append(l[j])
        func(l,l2,j+1,n)
        l2.pop()
func(l,[],0,n)
  
  


        
        
