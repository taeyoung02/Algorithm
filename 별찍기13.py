n=int(input())

for k in range(-n+1, n):
    for i in range(n-abs(k)):
        print("*", end='')
    print("\n", end='')