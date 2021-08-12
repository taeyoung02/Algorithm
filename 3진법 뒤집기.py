def solution(n):
    answer = 0
    three = ""
    while int(n) != 0:
        three = str(n % 3) + three
        n //= 3 # 부동소수점

    a = 1
    for i in three:
        answer += a * int(i)
        a *= 3

    return answer

print(solution(45))