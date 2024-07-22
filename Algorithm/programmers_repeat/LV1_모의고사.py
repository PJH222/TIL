def solution(answers):
    answer = []
    a1 = [1,2,3,4,5] * (10000//5)
    a2 = [2, 1, 2, 3, 2, 4, 2, 5] * (10000//10)
    a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5,] * (10000//10)

    a , b , c = 0 , 0 , 0
    # print(a1)
    for i in range(len(answers)):
        if answers[i] == a1[i]:
            a += 1
        if answers[i] == a2[i]:
            b += 1
        if answers[i] == a3[i]:
            c += 1

    tmp = [a,b,c]
    tmp2 = sorted(tmp, reverse=True)

    if tmp.count(tmp[0]) == 2:





    return answer

solution([1,2,3,4,5]	)