def solution(N, stages):
    answer = []
    stages.sort()
    denominator = 0
    arr = [0] * N
    pctg = [0] * N
    for i in reversed(stages):
        denominator += 1
        if i <= N:
            arr[i - 1] += 1
            pctg[i - 1] = arr[i - 1] / denominator

    for i in range(N):
        pctg[i] = [pctg[i], N-i]
    pctg.sort()
    answer = [N-i[1]+1 for i in pctg]
    answer.reverse()
    return answer
# 34215
print(solution(	5, [2, 1, 2, 6, 2, 4, 3, 3]))
