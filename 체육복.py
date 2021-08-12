def solution(n, lost, reserve):
    re = [r for r in reserve if r not in lost]
    lo = [l for l in lost if l not in reserve]
    for i in re:
        if i - 1 in lo:
            lo.remove(i - 1)  # for문에서 쓰고있는 배열 건드리면 안됨
        elif i + 1 in lo:
            lo.remove(i + 1)

    answer = n - len(lo)
    return answer