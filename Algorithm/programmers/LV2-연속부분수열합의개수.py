# https://school.programmers.co.kr/learn/courses/30/lessons/131701

def solution(elements):
    answer = 0
    reset_list = elements * 2
    # print(reset_list)
    nums = []
    cnt = 0
    for i in range(len(elements)):
        a = 0
        for j in range(len(elements)):
            a += reset_list[i+j]
            nums.append(a)
            #sum(슬라이스) 시간 다 먹는 듯..
            # if a not in nums:
            #     nums.append(a)
            #     cnt += 1
    # print(reset_list, len(reset_list))
    return len(set(nums))

print(solution([7,9,1,1,4]	))
# print(solution([1000 for i in range(1000)]))