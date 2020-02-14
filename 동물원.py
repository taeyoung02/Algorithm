n = int(input())
d=[0]*100000 #d[i]번째에 동물이 있을때
s=[0]*100000 #d[0]+..+d[i]
d[0]=2
s[0]=3
d[1]=4
s[1]=s[0]+d[1]

for i in range(2,n):
    d[i]=d[i-1]+2*s[i-2]
    s[i]=s[i-1]+d[i]
    d[i]%=9901
    s[i]%=9901

print(s[n-1])