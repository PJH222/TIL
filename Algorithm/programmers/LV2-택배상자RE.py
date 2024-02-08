from collections import deque
# 보조
def solution(order):
    answer = 0
    stack = deque()
    result = []
    cnt = 0 # 진짜 index
    for i in range(1,len(order) + 1): # 박스가 주어지는 순서
        if len(stack) == 0:
            if i != order[cnt]:
                stack.appendleft(i) # 현재 주어진 택배를 추가하기
            else:
                answer += 1
                cnt += 1

        else:
            if i != order[cnt] and i != stack[0]:
                stack.appendleft(i)

            elif i == order[cnt]:
                answer += 1
                cnt += 1
                while 1:
                    if len(stack) == 0: # 길이가 0 이면 종료
                        break
                    # print(stack, cnt, result)
                    a = len(stack)
                    if order[cnt] == stack[0]:
                        answer += 1
                        cnt += 1
                        stack.popleft()
                    b = len(stack)

                    if a == b: # 변함없으면 종료
                        break

            elif i == stack[0]:
                stack.popleft()
                answer += 1
                cnt += 1

    # print(result)



            # if i == stack[0]:
            #     stack.popleft()
            #     answer += 1
            #     cnt += 1


        # print(stack,cnt,result)
        # print("현재 idx, order에서의 순서, 현재 주어진 박스")
        # print(cnt,"       ",order[cnt],"         ",i)
    # else:


    return answer

print(solution([4, 3, 1, 2, 5]	))
print(solution([5, 4, 3, 2, 1]	))