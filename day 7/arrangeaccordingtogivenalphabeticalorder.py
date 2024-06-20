n=2
s="polikujmnhytgbvfredcxswqaz"
s1="abbcdd"
'''s="qwryupcsfoghjkldezxvbintma"
s1="ativedoc"'''
d={}
s2=""
s1=list(s1)
s=list(s)
print(s1)
for i in range(len(s)):
    if s[i] in s1:
           s2+=(i*s1.count(i))
print(s2)      
        
