# https://school.programmers.co.kr/learn/courses/30/lessons/42628
import heapq
from heapq import nlargest,nsmallest
def solution(operations):
    answer = []
    nums = []
    for i in operations:
        lis = list(i.split(" "))
        for j in range(len(lis)):
            if lis[j] == "I":
                nums.append(int(lis[j+1]))
            elif nums and lis[j] == "D" and lis[j+1] == "1":
                nums.remove(max(nums))
            elif nums and lis[j] == "D" and lis[j+1] == "-1":
                nums.remove(min(nums))
            # print(nums)
    return [int(max(nums)),int(min(nums))] if nums else [0,0]

print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]	))
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]	))
# print(solution(["I " + str(x) for x in range(300000)] + ["D 1", "D -1"] * 100000 + ["I " + str(x) for x in range(300000, 600000)] + ["D 1", "D -1"] * 100000	))
print(solution(["I " + str(x) for x in range(30000)] + ["D 1", "D -1"] * 100000 + ["I " + str(x) for x in range(30000, 60000)] + ["D 1", "D -1"] * 100000	))