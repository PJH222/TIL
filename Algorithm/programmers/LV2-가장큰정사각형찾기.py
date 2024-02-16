# https://school.programmers.co.kr/learn/courses/30/lessons/12905

def solution(board):
    answer = 0
    best = 0
    dp_table = [[0] * (len(board[0]) + 1) for i in range(len(board) + 1)]
    # print(dp_table)

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                dp_table[i][j] = min(dp_table[i - 1][j], dp_table[i][j - 1], dp_table[i - 1][j - 1]) + 1
                if dp_table[i][j] > best:
                    best = dp_table[i][j]

    return best ** 2