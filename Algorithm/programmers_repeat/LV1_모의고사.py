def solution(answers):
    answer = []
    a1 = [1,2,3,4,5] * (10000)
    a2 = [2, 1, 2, 3, 2, 4, 2, 5] * (10000)
    a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (10000)

    a , b , c = 0 , 0 , 0

    # print(a1)
    for i in range(len(answers)):
        if answers[i] == a1[i]:
            a += 1
        if answers[i] == a2[i]:
            b += 1
        if answers[i] == a3[i]:
            c += 1

    dict = [("1",a),("2",b),("3",c)]
    d = sorted(dict, key = lambda x:x[1], reverse=True)
    tmp = []
    for i in range(3):
        tmp.append(d[i][1])

    # print(d,tmp)

    for i in tmp:
        if tmp.count(i) == 3:
            answer = [1,2,3]
            break

        elif tmp.count(i) == 2 and i == max(tmp):
            answer.append(int(d[0][0]))
            answer.append(int(d[1][0]))
            break

        elif i == max(tmp) and tmp.count(i) == 1:
            answer.append(int(d[0][0]))
            break

    # print(answer,dict)
    return answer

solution([1,2,3,4,5]	)
solution([1,3,2,4,2]	)
solution([3,2,4,3,2]	)