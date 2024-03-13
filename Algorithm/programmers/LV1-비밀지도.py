def solution(n, arr1, arr2):
    answer = []
    matrix1 = []
    matrix2 = []

    for i in arr1:
        binary = format(i,'b')
        if len(binary) < n:
            diff = n - len(binary)
            binary = '0' * diff + str(binary)
        matrix1.append(list(binary))

    for i in arr2:
        binary = format(i,'b')
        if len(binary) < n:
            diff = n - len(binary)
            binary = '0' * diff + str(binary)
        matrix2.append(list(binary))

    for col in range(n):
        tmp = ''
        for row in range(n):
            if matrix1[col][row] == '1' or matrix2[col][row] == '1':
                tmp += "#"
            else:
                tmp += ' '
        answer.append(tmp)

    # a = format(n,'b')


    return answer

print(solution(5,[9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution(6,[46, 33, 33 ,22, 31, 50],[27 ,56, 19, 14, 14, 10] ))
