
def solution(n):
    answer = 0

    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 2

    for i in range(2,n):
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000007
        if i == n - 1:
            return dp[i]


print(solution(1)) # 1
print(solution(2)) # 2
print(solution(3)) # 3
print(solution(4)) # 5
print(solution(5)) # 8
print(solution(6)) #
print(solution(100))
