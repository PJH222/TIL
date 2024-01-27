import time
def solution(number, k):
    zz = time.time()
    result = []
    max = 0
    b = list(number)
    a = list(number)
    a.sort(reverse=True) # 최대값 리스트

    for i in range(len(a)):
        o = b.index(a[i])
        if o >= k + 1:  # 보통 숫자는 첫째 자리가 가장 큰 수 일수록, 전체 숫자가 클 확률이 높다.
            continue                # 혹시나 길이가 짧아 숫자를 못만들 경우 넘기기
        else:
            new_number = b[o:]  # 첫자리 숫자가 큰 것부터 확인
            sec_number = b[o:]
            if int(new_number[0]) >= max:
                max = int(new_number[0])
            else:
                continue
            new_k = k  - o      # 숫자를 몇개 지울지에 대한 새로운 상수
            cnt = 0                         # 여태 몇개 지웠는지 count할 변수
            delete = []                     # 지워야 하는 원소의 리스트

            for j in range(len(new_number) - 2):                # 3개 비교해서 중간에 작은 값을 지우는게 베스트,,,

                if ((int(new_number[j]) > int(new_number[j + 1])) and (int(new_number[j + 1]) < int(new_number[j + 2]))
                        or (int(new_number[j]) <= int(new_number[j + 1]) and int(new_number[j + 1]) < int(new_number[j + 2]))):
                    delete.append(new_number[j + 1])
                    cnt += 1

                if cnt == new_k:
                    for _ in delete:
                        new_number.remove(_)
                    zx = time.time()
                    print("걸리는 시간 :",zx - zz)
                    return ((''.join(new_number)))
                    # print(int(''.join(new_number)))


            else:       # 만약 3개 비교가 불가하여 이전 for문에서 그냥 넘어온 경우
                c = sorted(b[o:])
                # print(c)
                for _ in range(new_k):
                    sec_number.remove(c[_])

                zx = time.time()
                print("걸리는 시간 :",zx - zz)

                # print(''.join(sec_number))
                # return (''.join(sec_number))

    # return max(result)


a = ["9" for i in range(999999)] + ["1"]
solution(''.join(a),9999)


# print(solution("1924"	,2))
# print(solution("1231234"	,3)) #
# print(solution("4177252841"	,4)) #
# print(solution("4177252841"	,2)) # 77 ~
# print(solution("4177252841"	,1)) # 477 ~
# print(solution("999"	,2))
# print(solution("998"	,2))
# print(solution("9987654321"	,2))
# print(solution("9988888"	,1))
# print(solution("123456789"	,2))
# print(solution("989"	,1))
# print(solution("090"	,1))
# print(solution("090"	,2))
# print(solution("3902"	,2))
# print(solution("39102"	,2))
# print(solution("0090"	,2))
# print(solution("18909098"	,2))
# print(solution("18909098"	,5)) # 999
# print(solution("18290697089918"	,6)) # 99789918

