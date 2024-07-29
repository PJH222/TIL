def solution(k, m, score):
    answer = 0
    ss = sorted(score,reverse=True)
    # print(ss)

    for i in range(1,len(ss)//m + 1):
        # print(ss[i * m - 1])
        if ss[i * m - 1] > k:
            answer += k * m
        else:
            answer += ss[i * m - 1] * m

    # print(answer)


    return answer

solution(3,4,[1, 2, 3, 1, 2, 3, 1]	)
solution(4,3,[4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]	)