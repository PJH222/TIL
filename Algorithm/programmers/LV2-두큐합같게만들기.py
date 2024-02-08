from collections import deque

def solution(queue1, queue2):
    answer = 0
    all_que = deque()
    summ = (sum(queue1) + sum(queue2))
    all_que += (queue1 + queue2)

    if summ % 2 != 0:
        return -1
    # 우선 찾아야 할 것, 반반 나눈 값을 만들 수 있는 것인가?
    result = sum(list(all_que)[0:len(queue1) + 1])
    left = deque()
    zip = []
    # print(all_que)
    for i in list(all_que):
        print(all_que, result, i)
        if result == summ // 2:
            zip.append(answer)
            print("집가고싶다..")

        result += i
        left.append(i)

        if result > summ//2:
            answer += 1
            a = all_que.popleft()
            result -= a
            all_que += [a]

            if len(left) > 0:
                left.popleft()

            if result == summ//2:
                zip.append(answer)
                print("집가고싶다..")
    print(zip)



print(solution([3, 2, 7, 2],	[4, 6, 5, 1]))
# print(solution([1, 2, 1, 2]	,[1, 10, 1, 2]))
# print(solution([1, 1]	,[1, 5]))
# print(solution([1, 1]	,[2, 5]))