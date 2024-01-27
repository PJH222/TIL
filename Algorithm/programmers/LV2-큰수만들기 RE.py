import heapq
def solution(number, k):
    answer = ''
    first_max = 0
    max = 0
    a = list(number)

    for i in range(k+1):
        new_number = a[i:]
        if int(new_number[0]) < int(first_max):
            continue
        elif int(a[i]) > int(first_max):
            first_max = a[i]

        cnt = 0
        delete = []

        for j in range(len(new_number) - 2):
            if (int(new_number[j]) > int(new_number[j+1])
                    and int(new_number[j+1]) < int(new_number[j+2])):
                delete.append(new_number[j+1])
                cnt += 1
                print(delete, cnt, k - i)

            # 이거왜걍 넘어가냐고 ~~~~
            if cnt == k - i:
                # print(delete, new_number)
                # print(''.join(new_number), max)
                for x in delete:
                    new_number.remove(x)
                else:
                    if max < int(''.join(new_number)):
                        max = int(''.join(new_number))
                break
        else:
            for y in range(len(number)):
                if len(new_number) != len(number) - k:
                    new_number.pop()
                else:
                    if max < int(''.join(new_number)):
                        max = int(''.join(new_number))
                    break

    return str(max)






    # # 이 방식의 문제점은 전체 숫자가 큰지 작은지를 판별할 수가 없음..
    # for i in range(len(number) - 1):
    #     if k == 0:
    #         answer +=
    #         break
    #
    #     if number[i] >= number[i+1]: # 이딴식으로 해버리면 큰수 안나오면 답 안나옴
    #         answer += number[i]
    #         k -= 1
    #     else:
    #         continue


# print(solution("1924"	,2))
# print(solution("1231234"	,3)) #
# print(solution("4177252841"	,4)) #
# print(solution("4177252841"	,1)) # 477 ~
# print(solution("4177252841"	,2)) # 77 ~
# print(solution("999"	,2))
# print(solution("998"	,2))
# print(solution("9987654321"	,2))
# print(solution("9988888"	,1))
# print(solution("123456789"	,2))
# print(solution("989"	,1))
print(solution("090"	,1))
print(solution("090"	,2))
print(solution("3902"	,2))
print(solution("39102"	,2))





