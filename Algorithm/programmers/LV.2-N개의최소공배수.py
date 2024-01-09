# https://school.programmers.co.kr/learn/courses/30/lessons/12953

def solution(arr):
    result = []
    answer = 1
    
    #어차피 100까지의 자연수 이니까 범위 안 의 소인수를 넣어 두자..
    nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    diction = {}
    for i in arr:
        for j in range(len(nums)):
            for k in range(7, 0, -1):
                if i % (nums[j] ** k) == 0 and nums[j] not in diction:
                    diction[nums[j]] = k
                elif i % (nums[j] ** k) == 0 and nums[j] in diction:
                    if diction[nums[j]] < k :
                        diction[nums[j]] = k

    for k,v in diction.items():
        answer *= k**v

    return answer

print(solution([2, 6, 8, 14])) # 2 : 3, 3 : 1, 7 : 1
print(solution([1, 2, 3]))
