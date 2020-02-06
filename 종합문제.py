#2
f=open("abc.txt",'w')
for i in range(3):
    data=input()
    f.write(data+'\n')
f.close()
f=open("abc.txt",'r')

lines=f.readlines()
f.close()

lines.reverse()

for line in lines:
    print(line.strip())
   