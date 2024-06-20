s=input()
s1=""
for i in range(len(s)):
 s1=""
 for k in range(i,len(s)):
  s1+=s[k]
  if len(s1)==1:
      print(s1)
  for j in range(k+1,len(s)):
      print(s1+s[j])
