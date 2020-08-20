def solution(*phone_book):
    answer = True
    dic=dict()
    dic2=dict()

    arr = [list() for _ in range(21)]
    

    for i in phone_book:
        arr[len(i)].append(i)
        
    print(arr)
    for i in range(1,21):
            for j in arr[i]:
                for k in range(i+1,21):
                        for q in arr[k]:
                            print(q)
                            if j == q[0:len(j)]:
                                return False

    print(answer)


solution("12","13","1345","154","1343")

# def solution(*phoneBook):
#     phoneBook = sorted(phoneBook)
#     print(phoneBook)
#     for p1, p2 in zip(phoneBook, phoneBook[1:]):
#         print(p1, p2)
#         if p2.startswith(p1):
#             return False
#     return True


# solution("12","13","1345","154","1343")

