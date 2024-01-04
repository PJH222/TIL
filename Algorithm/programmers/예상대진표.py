
# https://school.programmers.co.kr/learn/courses/30/lessons/12985


#커트라인 제일 끝에 도달했을 때, 몇번 대전이 발생하는지 바로 구할 수 있음.
def solution(n,a,b):
    answer = 0


    print(a,b)

    return answer

print(solution(8,1,7))          # 3
print(solution(8,4,7))          # 3
print(solution(8,1,4))          # 2
print(solution(16,1,4))          # 2
print(solution(16,5,8))          # 2

# a,b 값이 서로 제일 멀리 존재해도, n이 커질 때 answer += 1 임 / 상관없는 모든 값을 제거할 수 있으면 되는데...
# 1 2 / 3 4
# 1 2
# 1

# 1 2 3 4 / 5 6 7 8
# 1 2 / 3 4
# 1 2
# 1

# 1 2 3 4 5 6 7 8 / 9 0 1 2 3 4 5 6
# 1 2 3 4 / 5 6 7 8
# 1 2 / 3 4
# 1 2
# 1
