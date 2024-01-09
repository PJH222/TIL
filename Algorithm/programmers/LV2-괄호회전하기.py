# https://school.programmers.co.kr/learn/courses/30/lessons/76502

def stacks(list):
    stack = []

    for i in list:
        if len(stack) == 0:
            stack.append(i)
        elif stack[-1] == "(" and i == ")":
            stack.pop()
        elif stack[-1] == "{" and i == "}":
            stack.pop()
        elif stack[-1] == "[" and i == "]":
            stack.pop()
        else:
            stack.append(i)

    if len(stack) == 0:
        return 1
    else:
        return 0
def solution(s):
    answer = 0
    stack = []
    ss = list(s) * 2
    # ss.pop()
    for i in range(len(s)-1):
        answer += stacks(ss[i:i+len(s)])
        # print(stacks(ss[i:i+len(s)]),ss[i:i+len(s)])

    return answer

print(solution("[](){}"	))
print(solution("}]()[{"	))
print(solution("[)(]"	))
print(solution("}}}"	))
