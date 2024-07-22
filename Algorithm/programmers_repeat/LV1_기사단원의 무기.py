def solution(number, limit, power):
    answer = 0

    for i in range(1,number+1):
        tmp = 0
        # print("현재 기사 번호 :",i)
        aa = []
        for j in range(1,int(i**(1/2)) + 1):
            if i%j == 0:
                tmp += 1
                aa.append(j)
                if j**2 != i: # 이 원리가 뭔지 모르겠다...
                    tmp += 1

        else:
            # print(tmp)
            # print(aa)
            if tmp <= limit:
                answer += tmp
            else:
                answer += power

        # print(tmp)
    print(answer)
    print()

    return answer

solution(5,3,2)
solution(10,3,2)
solution(25,3,2)
