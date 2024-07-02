def solution(a, b, n):
    answer = 0
    for i in range(1000000):
        if n//a == 0:
            break
        else:
            answer += n//a * b # 현재 상태에서 추가로 받는 공병

            aa = n // a # 몫
            bb = n % a # 나머지

            n -= aa * a # 콜라를 이미 내었기 때문에 n에서 빼주기
            n += aa * b

    print(answer)


    return answer

solution(2,1,20) # 19
solution(3,1,20) # 9