def solution(n, m, section):
    answer = 0

    indict = 0

    for i in section:
        if i > indict:
            indict = i + m - 1
            answer += 1

    print(answer)


    return answer

solution(8,4,[2,3,6])
solution(5,4,[1,3])
solution(4,1,[1,2,3,4])
