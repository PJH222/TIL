def solution(routes):
    answer = 0
    result = []

    routes.sort()

    for left,right in routes:
        result.append(list(range(left,right+1)))

    print(result)
    return answer

# print(solution([[0,20],[2,3],[3,19],[17,18]]))


print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]	)) # 2
# print(solution([[-1,1],[-1,2],[-1,3],[-1,4],[-1,5],[-1,6]]))
# print(solution([[-1,1],[-1,1],[-1,1],[-1,1],[-1,1],[-1,1]]))
