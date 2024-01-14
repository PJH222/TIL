# https://school.programmers.co.kr/learn/courses/30/lessons/42587
import heapq

def solution(priorities, location):
    answer = 0
    answer_list = [0 for i in range(len(priorities))]
    cnt = 1 # 절대 좌표
    x = 0 # 상대 좌표

    for i in range(9,0,-1):
        howmuchin = 0 # 번호 바뀔 때 마다 초기화
        if 0 not in answer_list:
            break

        if i in priorities:
            #가변 좌표
            a = priorities.count(i)
            for j in range(x,len(priorities)): #뒤에서 실행
                # print(answer_list,a,x)
                if priorities[j] == i and howmuchin != a :
                    answer_list[j] = cnt
                    cnt += 1
                    howmuchin += 1
                    if howmuchin == a:
                        if j == len(priorities) - 1:
                            x = 0 #가장 마지막에 i를 찾은 경우에는 x를 0으로 초기화

                        else:
                            x = j + 1 #여기서 왜 x = 4로 안넘억 가지지..?


                # if howmuchin == a: #앞에서 다찾았으면 그냥 다음 i로 넘어가기
                #     break

            for j in range(x):  # 뒤에서 실행
                # print(answer_list, a, x)
                if priorities[j] == i and howmuchin != a:
                    answer_list[j] = cnt
                    cnt += 1
                    howmuchin += 1
                    if howmuchin == a:
                        if j == len(priorities) - 1:
                            x = 0  # 가장 마지막에 i를 찾은 경우에는 x를 0으로 초기화
                        else:
                            x = j + 1  # 여기서 왜 x = 4로 안넘억 가지지..?

    return answer_list[location]





print(solution([2, 1, 3, 2]	, 2))
print(solution([1, 1, 9, 1, 1, 1]	,0))
print(solution([8, 1, 9, 9, 8, 1]	,0))
