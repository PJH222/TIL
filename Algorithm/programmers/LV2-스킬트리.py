def solution(skill, skill_trees):
    answer = 0
    all_of_skill_tree = []
    for i in range(1,len(skill)+1):
        all_of_skill_tree.append(skill[:i])

    for i in skill_trees:
        skill_set = []
        idx = 0
        cnt = 0

        for j in i:
            # print(i,idx, len(i) - 1)
            # skill에 있는 모든원소를 순서대로 만난 경우
            # if ''.join()

            if skill[idx] == j:
                idx += 1
                skill_set.append(j)

            elif skill[idx] != j and j in skill: # 뒤에 나와야할 거 앞에 나올 경우
                break

            elif skill[idx] != j and j not in skill:
                cnt += 1

            if ''.join(skill_set) == skill: # 대충 만든게 답나오면 끝내기
                answer += 1
                break
        else:
            answer += 1



    return answer

print(solution("CBD"	,["BACDE", "CBADF", "AECB", "BDA"]	))