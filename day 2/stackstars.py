s=input()
st=[]
for i in range(len(s)):
    if st and s[i]=="*":
        st.pop()
    else:
        st.append(s[i])
print("".join(st))
    
        
