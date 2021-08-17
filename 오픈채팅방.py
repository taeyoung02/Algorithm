def solution(record):
    result={}
    ans=[]
    cnt=0
    for i in record:
        s=i.split()
        if s[0]=="Enter":
            result[s[1]] = s[2]
        elif s[0]=="Change":
            result[s[1]] = s[2]

    for i in record:
        s=i.split()
        if s[0]=="Enter":
            ans.append(result[s[1]]+"님이 들어왔습니다.")
        elif s[0]=="Leave":
            ans.append(result[s[1]]+"님이 나갔습니다.")

    return ans

solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])