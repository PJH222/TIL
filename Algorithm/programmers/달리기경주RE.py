# https://school.programmers.co.kr/learn/courses/30/lessons/178871#
def solution(players, callings):
    answer = []

    players_dict = {player : int(i) for i , player in enumerate(players)}

    for call in callings:
        now_rank = players_dict[call]
        players_dict[call] -= 1
        players_dict[players[now_rank-1]] += 1

        players[now_rank-1] , players[now_rank] = call , players[now_rank-1]



    return players

