n=input()
s=str(n)
s1=s[::-1]
if s==s1:
    print(s)

sm=s[:len(s)//2]
sr=sm+sm[::-1]
print(sr)
    
