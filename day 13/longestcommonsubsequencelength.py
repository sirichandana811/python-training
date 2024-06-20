s1=input()
s2=input()
l=[]
m=[]
for i in range(len(s1)+1):
   l=[0]*(len(s2)+1)
   m.append(l)
for i in range(1,len(s1)+1):
    for j in range(1,len(s2)+1):
        if (s1[i-1]==s2[j-1]):
            m[i][j]=m[i-1][j-1]+1
        else:
            m[i][j]=max(m[i-1][j],m[i][j-1])
print(m[i][j])

s3=""
i=len(s1)
j=len(s2)
while i!=0 and j!=0:
        if s1[i-1]==s2[j-1]:
            s3+=s1[i-1]
            i=i-1
            j=j-1
        else:
            if m[i-1][j]==m[i][j]:
                i=i-1
            else:
                j=j-1
print(s3)               
