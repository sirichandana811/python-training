n=int(input())
l=[]
for i in range(n):
    n1=int(input())
    s=input()
    if n1==1:
        l.append(s)
    if n1==2:
        if l and s in l:
            print("true")
        else:
            print("false")
    if n1==3:
        c=0
        if l:
         for i in range(len(l)):
            if l[i] not in l[:i] and l[i][:len(s)]==s:
                c+=1   

        print(c)
    if n1==4:
        if l and  s in l:
            l.remove(s)
        
