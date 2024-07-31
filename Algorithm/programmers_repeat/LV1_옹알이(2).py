from itertools import product as pr

def solution(babbling):
    answer = 0
    tmp = ["aya", "ye", "woo", "ma"]
    tmp3 = []

    for i in tmp:
        tmp3.append(i * 2)
    # print(tmp3)
    result = []

    for index in range(1,10):
        tmp2 = list(map(''.join, pr(tmp,repeat=index)))
        for i in tmp2:
            for j in tmp3:
                if j in i:
                    break
            else:
                result.append(i)

    for i in babbling:
        if i in result:
            answer += 1

    print(answer)

    return answer

solution(["aya", "yee", "u", "maa"])
solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]	)
solution(["maya"]	)