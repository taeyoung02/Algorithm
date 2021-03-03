def solution(genres, plays):
    dic=dict()
    rdic=dict()
    for k,(i,j) in enumerate(zip(genres,plays)):
        try:
            dic[i].append((j,k))
        except:
            dic[i]=[(j,k)]
        try:
            rdic[i]+=j
        except:
            rdic[i]=j
            
    rdic=sorted(rdic.items(), key = lambda x: x[1], reverse=True)
    answer = []
    for i in rdic:
        dic[i[0]].sort(reverse=True)
        answer.append(dic[i[0]][0][1])
        answer.append(dic[i[0]][1][1])
    return answer


solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])