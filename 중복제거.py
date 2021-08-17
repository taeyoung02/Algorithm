def solution(arr):
    print(arr)
    sorted(list(set(arr)), key=lambda x: x.index)
    print(arr)
    return arr[:,0]

print(solution([1,1,5,3]))