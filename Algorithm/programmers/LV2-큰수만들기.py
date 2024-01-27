# 숫자를 제거하는 알고리즘 구성을 어떻게 하지?

    # i) 최대한 큰 숫자가 1의 자리에 들어올 수 있게끔 알고리즘을 구성해야함

    # length = len(number) - k # k만큼 number에서 숫자 소거한 길이
    # for i in range(len(number)):

    # insert는 해당 index가 존재하지 않아도 대충 순서에 맞춰서 들어가짐.,,
    # a = []
    # a.insert(2,"A")
    # print(a)
    # 여기서 필요한 내용은 아닌 것 같다,,,
    # 아무리 생각해도 heappop 써서 최소값을 삭제해가면서 해야하는 것 같은데,,,
import heapq as hq

def solution(number, k):
    # 1백만 단위라 for문 하나로 끝내야함,,,
    answer = ''
    a = list(number)
    max = 0
    for i in range(len(number)):
        if k != 0:
            new_number = a[i:]
            min = new_number[0]
            cnt = 0
            for j in range(1,len(new_number)):
                if cnt == k:
                    if max < int(''.join(answer)):
                        max = int(''.join(answer))
                        k -= 1
                        break

                if new_number[j] < min:
                    min = new_number[j]
                    cnt += 1

                else:
                    answer += new_number[j]
        else:
            break

    return max

print(solution("1924"	,2))
print(solution("1231234"	,3))
print(solution("4177252841"	,4))
