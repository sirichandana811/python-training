s=input()
n=int(input())
s1=""
for i in s:
    n1=ord(i)-(n%26)
    if n1<97:
        n1=n1+26
    s1+=chr(n1)

print(s1)
