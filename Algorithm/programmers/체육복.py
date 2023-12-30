# https://school.programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    answer = 0
    answer_list = [i+1 for i in range(n)]
    fool_boy_number = len(lost)
    good_boy_number = len(reserve)
    for i in lost:
        if i in answer_list:
            answer_list.remove(i)

    loss = sorted(lost)
    ress = sorted(reserve)

    for i in range(len(loss)):
        if loss[i] in ress:
            ress.remove(loss[i])
            answer_list.append(loss[i])

        elif loss[i]-1 in ress:
            answer_list.append(loss[i])
            ress.remove(loss[i]-1)

        elif loss[i]+1 in ress:
            answer_list.append(loss[i])
            ress.remove(loss[i] + 1)



    return len(answer_list)
print(solution(5, [4, 5], [3, 4])) #4
solution(5,[2, 4],[1, 3, 5])
solution(5,[2, 4],[3])
solution(3,[3],[1])


