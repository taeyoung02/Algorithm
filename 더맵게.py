import heapq as h

def solution(scoville, K):
    answer = 0
    l=len(scoville)
    h.heapify(scoville)

    for i in range(l):
        a=h.heappop(scoville)
        if a>=K:
            return answer
        else:
            if scoville==[]:
                return -1
            answer+=1
            b=h.heappop(scoville)
            h.heappush(scoville, a+b*2)

    return -1