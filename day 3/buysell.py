l=[]


























































n=int(input())
n1=1
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end=" ")
        else:
            print(n1,end=" ")
            n1+=1
    print(" ")
        
        













































for i in range(6):
    l.append(int(input()))

b=l[0]
m=0
for i in l:
            if i<b:
                b=i
            elif i-b>m:
                m=i-b
print(m)




    
