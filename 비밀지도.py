def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        IJ = str(bin(i | j)[2:]) # 앞에는 0b가 붙음
        IJ = IJ.rjust(n - len(IJ), "0")

        IJ.replace("0", " ")
        IJ.replace("1", "#")

        answer.append(IJ[::-1])
    return answer

print(solution(5
,[9, 20, 28, 18, 11]
,[30, 1, 21, 17, 28]))