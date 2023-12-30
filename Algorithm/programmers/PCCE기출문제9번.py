# https://school.programmers.co.kr/learn/courses/30/lessons/250125#

def solution(board, h, w):
    answer = 0
    color = board[h][w]
    # W 따로 h 따로 2번씩, 즉 총 4번만 측정하면 되지 않을까...?

    if w == 0:
        if board[h][w + 1] == color:
            answer += 1
    elif w == len(board) - 1:
        if board[h][w - 1] == color:
            answer += 1
    else:
        if board[h][w + 1] == color:
            answer += 1
        if board[h][w - 1] == color:
            answer += 1

    if h == 0:
        if board[h + 1][w] == color:
            answer += 1
    elif h == len(board) - 1:
        if board[h - 1][w] == color:
            answer += 1
    else:
        if board[h + 1][w] == color:
            answer += 1
        if board[h - 1][w] == color:
            answer += 1

    return answer