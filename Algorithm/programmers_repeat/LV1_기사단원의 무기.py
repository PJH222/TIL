def solution(number, limit, power):
    answer = 0

    for i in range(1,number+1):
        tmp = 0
        for j in range(1,int(i**(1/2)) + 1):
            if i%j == 0:
                tmp += 1
                if j**2 != i:
                    tmp += 1

        else:
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
