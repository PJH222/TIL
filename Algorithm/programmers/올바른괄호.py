# https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    answer = True
    compare_box = []

    for i in s:
        if len(compare_box) == 0:
            compare_box.append(i)

        elif compare_box[-1] == "(" and i == ")":
            compare_box.pop()

        elif compare_box[-1] == i:
            compare_box.append(i)

        elif compare_box[-1] == ")" and i == "(":
            compare_box.append(i)

    print(compare_box)
    if len(compare_box)>0:
        answer = False

    return answer

print(solution("()()"	))
print(solution("(())()"	))
print(solution(")()("	))
print(solution("(()("	))

