string=input()
stack=[]

result=[]
i=0
for i in range(len(string)):
    if string[i] =='(':
        stack.append('(')

    elif string[i]==')':
        while stack[-1]!='(':
            print(stack.pop(),end='')
        stack.pop()

    elif string[i].isalpha():
        print(string[i], end='')
    
    else:
        if string[i]=='*' or string[i]=='/':
            while stack:
                if stack[-1]=='*' or stack[-1]=='/':
                    print(stack.pop(),end='')
                else: break
            stack.append(string[i])
        else:
            while stack and stack[-1]!='(':
                print(stack.pop(),end='') 
            stack.append(string[i])
        

while stack:
    print(stack.pop(),end='')

        
'''
A*(B+C)
ABC+*
'''
