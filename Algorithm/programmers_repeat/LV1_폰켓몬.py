def solution(nums):
    answer = 0

    b = len(set(nums))
    c = len(nums) // 2
    print(b,c)

    if b > c:
        answer = c
    else:
        answer = b

    return answer

solution([3,1,2,3]	)
solution([3,3,3,2,2,4]	)
solution([3,3,3,2,2,2]	)