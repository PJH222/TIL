from collections import deque

def solution(begin, target, words):
    answer = 1

    if target not in words:
        return 0

    check = [0] * len(begin) # 0인지 아닌지 빨리 찾는 용도
    stack = [[]] * len(begin) # 0,1,2 등 늘 하던대로 정리


    for i in range(len(target)):
        stack[i] = []

    for word in words:
        for j in range(len(word)):
            if word[j] == target[j] and word not in stack[j]:
                stack[j].append(word)
                check[j] = 1 # 0인지 아닌지 판별기

    que = deque()
    que.append(begin)
    visited = [0] * len(begin)
    result = []
    # print(stack)





    while que:
        a = que.popleft()
        for word in words:
            cnt = 0
            # 두글자 이상 다른 단어 거르기
            for j in range(len(word)):
                if a[j] != word[j]:
                    cnt += 1
                if cnt == 2:
                    break

            # 한 글자만 다른 단어는 하기 실행
            if cnt == 1:
                # print(word)
                for k in range(len(word)):
                    if word[k] == target[k] and visited[k] == 0 and word not in result:
                        visited[k] = 1
                        que.append(word)
                        result.append(word)
                        break
                else:
                    for k in range(len(word)):
                        if word in stack[k] and word not in result:
                            que.append(word)
                            result.append(word)
                            break
    print(result)
    visited = [0] * len(begin)
    answer = []
    for i in range(len(result) - 1):
        cnt = 0
        for j in range(len(begin)):
            if result[i][j] != result[i+1][j]:
                cnt += 1
            else:
                answer.append(result[i])


            if cnt == 2:
                result.remove(result[i])

        else:
            pass
    print(result)


    # print(visited,result)

    # for i in range(len(result) - 1):
    #     if


    return answer


def bfs(begin, target, words):
    pass


print(solution("hit"	,"cog"	,["hot", "dot", "dog", "lot", "log", "cog"]	))
# print(solution("hit"	,"cog"	,["hot", "dot", "dog", "lot", "log", "cog","ccs"]	))
# print(solution("hit"	,"cog"	,["hot", "dot", "dog", "lot", "log"]	))