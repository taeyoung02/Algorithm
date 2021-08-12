import math
import itertools
decimal = [False, False] + [True] * 2998
for i in range(2, math.ceil(math.sqrt(3000))):
    if decimal[i]:
        for j in range(2 * i, 3000, i):
            decimal[j] = False


answer = 0


def solution(nums):
    global answer
    arr = list(itertools.combinations(nums, 3))
    print(arr)
    for i in arr:
        if decimal[sum(i)]:
            answer+=1

    return answer
