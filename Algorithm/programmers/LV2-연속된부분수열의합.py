from collections import deque

def solution(sequence, k):
    answer = []
    lis = (deque(sequence))

    result = 0
    cnt = 0
    start = 0
    numberss = deque()
    minn = 100000000

    for i in list(lis)[::-1]:
        result += i
        cnt += 1
        numberss.append(i)
        if result > k:
            while result > k:
                result -= lis.pop()
                cnt -= 1
                start += 1
                numberss.popleft()
        if result == k:
            if cnt - 1 <= minn:
                minn = cnt - 1
                answer.append([len(sequence) - 1 - (start + cnt - 1), len(sequence) - 1 - start, cnt - 1])
                
    answer.sort()
    return answer[0][0:2]

            # print(result,k,answer,lis,numberss)




    return answer

print(solution([1, 2, 3, 4, 5]	,7))
print(solution([1, 1, 1, 2, 3, 4, 5]	,5))
print(solution([2, 2, 2, 2, 2]	,6))