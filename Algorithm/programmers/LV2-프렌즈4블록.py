import random
from string import ascii_uppercase
def solution(m, n, board):
    answer = 0

    # for 문 두개 쓸수 있겠는데...

    for i in range(len(board)):
        board[i] = list(board[i])

    # answer = make_zero_block(board, answer)
    return make_zero_block(board, answer)


def make_zero_block(board, answer):
    stack = []
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dy = [0,0,1,1]
    dx = [0,1,0,1]

    for i in range(len(board) - 1):
        for j in range(len(board[0]) - 1):
            for k in range(4):
                if board[i][j] == 0 or board[i][j] not in alpha:
                    break

                if board[i][j] == board[i+dy[k]][j+dx[k]]:
                    continue

                else:
                    break # k 들어간 for 문 깨고 나오기
            else:
                for k in range(4):
                    if (i+dy[k],j+dx[k]) not in stack:
                        stack.append((i+dy[k],j+dx[k]))

    else: # 현재 board 상태에서 4개짜리인 애들을 다 골라낸 이후임.
        # 추가할 거 다햇는데 할게 없었다면 return 하기
        if len(stack) == 0:
            # print(board)
            return answer
        
        # 남은거 있으면 answer에 제거한 개수만큼 더해주기
        answer += len(stack)

        for y,x in stack:
            board[y][x] = 0
        stack.clear()
        # print(board)
    # print(board,answer)
        return block_is_down(board,answer)


# 0이 있으면 위에서 한칸 내리기
def block_is_down(board,answer):
    end_point = True

    while end_point:
        chk = 0
        for i in range(len(board)):
            if 0 in board[i]:
                for j in range(len(board[0])):
                    if board[i][j] == 0 and i != 0 and board[i-1][j] != 0: # 가장 위에 존재하는 행이면 안되므로 i = 0은 제외
                        board[i][j] = board[i-1][j]
                        board[i - 1][j] = 0
                        chk = 1
                        # print(board)

                    # print(board, answer)
            else:
                continue

        if chk == 0:

            end_point = False

    # print(answer)
    return make_zero_block(board,answer)










# print(solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"]	))
# # 14
# print(solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]	))
# # # # 15
# print(solution(3,3,["AAA","AAA","CCC"]	))
# print(solution(4,3,["CCA","CCC","ACC","CCC"]	))
# print(solution(4,3,["CCC","CCC","CCC","CCC"]	))
# print(solution(4,3,["ACA","CAC","ACA","CCC"]	))
# print(solution(4,3,["CB","CB"]	))
# print(solution(4,3,["CCCC","BBCC","BBBC","CBBC"]	))
# print(solution(2,2,["aa","aa"]))
# print(solution(2,2,["aa","aa","AA","AA"]))
# print(solution(2,2,["AA","AA","aa","AA","AA"]))
# print(solution(2,2,["AAA","AaA","AAA","AaA","AAA"]))

print(solution(2,2,["AABBEE","AAAEEE","VAAEEV","AABBEE","AACCEE","VVCCEE" ]

))
