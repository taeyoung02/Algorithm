n=int(input())
s=input()
num=[0]*n
for i in range(n):
    num[i]=int(input())


stack=[]
for i in range(len(s)):
    if s[i].isalpha():
        stack.append(num[ord(s[i])-65])
    
    else:
        if s[i]=='*':
            a=stack.pop()
            b=stack.pop()
            stack.append(a*b)
        elif s[i]=='/':
            a=stack.pop()
            b=stack.pop()
            stack.append(b/a)
        elif s[i]=='+':
            a=stack.pop()
            b=stack.pop()
            stack.append(a+b)
        elif s[i]=='-':
            a=stack.pop()
            b=stack.pop()
            stack.append(b-a)

print('%.2f' % stack[0])