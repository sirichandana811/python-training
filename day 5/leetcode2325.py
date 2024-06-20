key="the quick brown fox jumps over the lazy dog"
msg="vkbs bs t suepuv"
d={}
j=97
d[" "]=" "
s=""
for i in key:
          if i!=" " and i not in d:
            d[i]=chr(j)
            j+=1
        
for i in msg:
            s+=d[i]
print(s)
