def solution(a, b):
    day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = 0
    if a > 1:
        for i in range(2, a+1):
            days += day[i - 2]
    print(days)
    days += (b - 1)

    days %= 7
    print(days)
    dayofweek = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]

    return dayofweek[days]

print(solution(2,1))