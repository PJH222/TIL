def solution(strings, n):
    answer = []

    aa = sorted(strings, key = lambda x : x[n])

    tmp = []
    for i in range(len(aa)):
        tmp.append(aa[i][n])

    # print(tmp)
    check = []
    for j in range(len(aa)):
        cnt = tmp.count(tmp[j])
        tmp2 = []
        if cnt > 1:
            for k in range(j,j + cnt):
                if aa[k] in check:
                    break
                else:
                    tmp2.append(aa[k])
                    check.append(aa[k])
            else:
                tmp3 = sorted(tmp2)
                for l in tmp3:
                    answer.append(l)
        else:
            answer.append(aa[j])

    print(answer)

    return answer

solution(["sun", "bed", "car"]	, 1)
solution(["abce", "abcd", "cdx"]	 , 2)