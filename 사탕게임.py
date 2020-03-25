n=int(input())
arr=list(list(input()) for i in range(n))#문자열을 list로 받으면 한개씩 쪼개짐
ans=1
def check(arr, x,y,option):
    global ans
    sum_1=1
    sum_2=1
    sum_3=1
    #right
    if option==2:
        for i in range(n-1):
            if arr[x][i]==arr[x][i+1]:
                sum_1+=1
                ans=max(ans,sum_1)
            else:
                sum_1=1
            
            if arr[x+1][i]==arr[x+1][i+1]:
                sum_2+=1
                ans=max(ans,sum_2)
            else:
                sum_2=1
            
            if arr[i][y]==arr[i+1][y]:
                sum_3+=1
                ans=max(ans,sum_3)
            else:
                sum_3=1
            
    elif option==1:
        for i in range(n-1):
            if arr[i][y]==arr[i+1][y]:
                sum_1+=1
                ans=max(ans,sum_1)
            else:
                sum_1=1
            
            if arr[i][y+1]==arr[i+1][y+1]:
                sum_2+=1
                ans=max(ans,sum_2)
            else:
                sum_2=1
            if arr[x][i]==arr[x][i+1]:
                sum_3+=1
                ans=max(ans,sum_3)
            else:
                sum_3=1

def swap(arr,a,b,c,d):
    arr[a][b],arr[c][d]=arr[c][d],arr[a][b]

if __name__ == "__main__":
    sum_4=1
    sum_5=1
    for i in range(n):
        for j in range(n-1):
            if arr[i][j]==arr[i][j+1]:
                sum_4+=1
                ans=max(sum_4,ans)
            else:
                sum_4=1

    for i in range(n):
        for j in range(n-1):    
            if arr[j][i]==arr[j+1][i]:
                sum_5+=1
                ans=max(sum_5,ans)
            else:
                sum_5=1
            
    for i in range(n-1):
        for j in range(n-1):
            swap(arr,i,j,i,j+1)
            check(arr,i,j,1)
            swap(arr,i,j,i,j+1)

            swap(arr,i,j,i+1,j)
            check(arr,i,j,2)
            swap(arr,i,j,i+1,j)
    print(ans)