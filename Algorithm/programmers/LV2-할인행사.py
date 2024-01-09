# https://school.programmers.co.kr/learn/courses/30/lessons/131127

def solution(want, number, discount):
    answer = 0
    a = len(discount)
    diction = {}

    for i in range(len(discount)-sum(number)+1):
        lis = discount[i:i + sum(number)]

        if set(want) == set(lis):
            for j in range(len(want)):
                if lis.count(want[j]) != number[j]:
                    break
                elif j == len(want) -1 and lis.count(want[j]) == number[j]:
                    answer+=1







    return answer

print(solution(["banana", "apple", "rice", "pork", "pot"]	,[3, 2, 2, 2, 1]	, ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]	 ))

print(solution(["apple"]	,[10]	,["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]	  ))

print(solution(["apple"]	,[10]	,["apple","apple","apple","apple","apple","apple","apple","apple","apple","banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana","apple","apple","apple","apple","apple","apple","apple","apple","apple","apple","apple","apple","apple","apple","apple","apple","apple","apple"]	  ))