import math
def sub(a,b):
    x=abs(a[0]-b[0])
    y=abs(a[1]-b[1])
    return [x,y]
def solution(numbers, hand):
    arr = [[0,0], [-1,3],[0,3], [1,3], [-1,2], [0,2], [1,2], [-1,1],[0,1], [1,1], [0,-1],[0,1]]
    answer = ''
    l=10
    r=11
    for i in numbers:
        if i == 1 or i==4 or i==7:
            answer+="L"
            l=i
        elif i == 3 or i==6 or i==9:
            answer+="R"
            r=i
        else:
            if sum(sub(arr[i],arr[r])) > sum(sub(arr[i],arr[l])):
                answer+="L"
                l=i
            elif sum(sub(arr[i],arr[r])) < sum(sub(arr[i],arr[l])):
                answer+="R"
                r=i
            else:
                if hand=="left":
                    answer+="L"
                    l=i
                if hand=="right":
                    answer+="R"
                    r=i

    return answer


print(solution([2,5,8,0],"right"))