# https://school.programmers.co.kr/learn/courses/30/lessons/42885


def solution(people, limit):
    answer = 0
    dict = {}
    people.sort()

    for i in people:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    while sum(dict.values()) >= 3:
        for i in range(len(dict.items())):
            print(dict)
            if sum(dict.values()) >= 3:
                maxd = max(dict)
                mind = min(dict)

                if maxd + mind == limit and dict[maxd] > 0 and dict[mind] > 0:
                    answer += 1
                    dict[maxd] -= 1
                    dict[mind] -= 1
                elif maxd + mind > limit and dict[maxd] > 0 and dict[mind] > 0:
                    answer += 1
                    dict[maxd] -= 1

                elif maxd * 2 == limit and dict[maxd] > 1:
                    answer += 1
                    dict[maxd] -= 2

                elif mind * 2 == limit and dict[mind] > 1:
                    answer += 1
                    dict[mind] -= 2

            # max, min 구하기
                for k, v in dict.items():
                    if dict[k] > dict[maxd] > 0 and k > maxd:
                        maxd = k

                    if dict[k] < dict[mind] and k < mind:
                        mind = k

            elif sum(dict.values()) == 2:
                for k, v in dict.items():
                    if sum(dict.keys()) > limit:
                        answer += 2
                        return answer
                    else:
                        answer += 1
                        return answer



            elif sum(dict.values()) == 1:
                answer += 1
                return answer

            else:
                return answer

    print(dict)

    return answer


# limit에 가장 가깝게 최소한으로 태우기...
# limit에 최대한 가깝게 만드는 알고리즘?
# sort로 정렬해서 작은것부터 딸딸 긁어 모으는게 낫나?
# 최소 + 최대로 합치는게 낫나?
# 탈 수 있는 사람은 최대 2명

# 조건 1) (limit - 최소무게) 이상인 사람은 무조건 혼자 타야한다.
# 조건 2) #순서는 안 중요함 최대한 몸무게 채워서 보낼 것.

print(solution([70, 50, 80, 50]	,100))              #3
print(solution([70, 80, 50], 100))  # 3
print(solution([40,45,50,60,60,80,50]	,100))      #5
# 5 ,
print(solution([40,40,50,60,60]	,100))              #3
print(solution([40,30,50,70,60]	,100))              #3
print(solution([45,45,45,55]	,100))                  #2
print(solution([45]	,100))                          #1
print(solution([40,40,60,60]	,100))                  #2