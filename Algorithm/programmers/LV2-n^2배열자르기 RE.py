def solution(n, left, right):
    answer = []

    for i in range(left,right+1):
        x = i%n
        y = i//n
        if x >= y:
            answer.append(x+1)
        else:
            answer.append(y+1)

        # answer.append(a)

    return answer

print(solution(3,2,5))
print(solution(4,7,14))
# print(solution(10**7,0,10**8)) #<< 이거 안됨

#1 2 3 4 5
#2 2 3 4 5
#3 3 3 4 5
#4 4 4 4 5
#5 5 5 5 5
