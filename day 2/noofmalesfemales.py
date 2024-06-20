s=input()
nm=0
nf=0
for i in s:
    if i=="m":
        nm+=1
    else:
        nm-=1
if nm>0:
    print("m")
elif nm<0:
    print("f")
else:
    print(0)
