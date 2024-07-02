def solution(n, arr1, arr2):
    answer = []
    maxx = 0 # 가장 긴 숫자의 길이를 판별하기 위함

    nw_arr1 = []
    nw_arr2 = []

    for i in arr1:
        aa = bin(i)[2:]
        if len(aa) > maxx:
            maxx = len(aa)
        nw_arr1.append(aa)

    # 두번 거쳐야 함. arr2에 길이가 더 긴 값이 존재 할 수 있음
    for i in arr2:
        aa = bin(i)[2:]
        if len(aa) > maxx:
            maxx = len(aa)
        nw_arr2.append(aa)

    for i in range(len(arr1)):
        if len(nw_arr1[i]) < maxx:
            nw_arr1[i] = '0' * (maxx - len(nw_arr1[i])) + nw_arr1[i]
        if len(nw_arr2[i]) < maxx:
            nw_arr2[i] = '0' * (maxx - len(nw_arr2[i])) + nw_arr2[i]

    for i in range(len(arr1)):
        tmp = ''
        for j in range(maxx):
            if nw_arr1[i][j] == '1' or nw_arr2[i][j] == '1':
                tmp = tmp + '#'
            else:
                tmp = tmp + ' '
        answer.append(tmp)

    print(answer)



    return answer

solution(5,[9, 20, 28, 18, 11]
,[30, 1, 21, 17, 28]
)
solution(6,[46, 33, 33 ,22, 31, 50]
,[27 ,56, 19, 14, 14, 10]
 )

