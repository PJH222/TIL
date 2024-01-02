# https://school.programmers.co.kr/learn/courses/30/lessons/67256

def solution(numbers, hand):
    answer = ''
<<<<<<< HEAD
    key_pad = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]

    L_w = [3,0] #Left finger where it is (x,y)
    R_w = [3,2] #Right finger where it is (x,y)
    L_sub = 0
    R_sub = 0

    for number in numbers:
        if number in [1,4,7]:
            answer += "L"
            for i in range(4):
                for j in range(3):
                    if key_pad[i][j] == number:
                        L_w[0] = i
                        L_w[1] = j
                        break

        elif number in [3,6,9]:
            answer += "R"
            for i in range(4):
                for j in range(3):
                    if key_pad[i][j] == number:
                        R_w[0] = i
                        R_w[1] = j
                        break
        else:
            for i in range(4):
                for j in range(3):
                    if key_pad[i][j] == number:
                        R_sub = abs(R_w[0]-i) + abs(R_w[1]-j)
                        L_sub = abs(L_w[0] - i) + abs(L_w[1] - j)
                        if L_sub > R_sub:
                            answer += "R"
                            R_w[0] = i
                            R_w[1] = j
                        elif L_sub < R_sub:
                            answer += "L"
                            L_w[0] = i
                            L_w[1] = j
                        else:
                            if hand == "right":
                                answer += "R"
                                R_w[0] = i
                                R_w[1] = j

                            else:
                                answer += "L"
                                L_w[0] = i
                                L_w[1] = j
        print(L_w, R_w, number)

=======
>>>>>>> 439beb103e41b087e5ef101a66ce72716d4247e9
    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]	,"right"	))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]	,"left"))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]	,"right"	))