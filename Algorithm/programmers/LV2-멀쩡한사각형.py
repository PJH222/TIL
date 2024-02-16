import time
def solution(w, h):
    answer = 1
    numbers = [2]
    a = time.time()
    for i in range(2, ):
        for j in range(2,int(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            numbers.append(i)

    print(numbers)
    print(time.time() - a)
    # 0.004534721374511719 - 1만
    # 2.9724719524383545 - 100만
    #

print(solution(2,3))