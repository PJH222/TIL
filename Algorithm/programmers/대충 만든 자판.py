# https://school.programmers.co.kr/learn/courses/30/lessons/160586

def solution(keymap, targets):
    answer = []

    for target in targets:
        result = 0
        min = 20000000
        for i in target:
            for key in keymap:
                if i in key and key.find(i) < min:
                    min =  key.find(i)
                else:
                    continue

            result += 1 + min
            min = 20000000
        if result < 20000001:
            answer.append(result)
        else:
            answer.append(-1)





    return answer

print(solution(["ABACD", "BCEFD"],["ABCD","AABB"]	))
print(solution(["AA"]	,["B"]	))
print(solution(["AGZ", "BSSS"]	,["ASA","BGZ"]	))