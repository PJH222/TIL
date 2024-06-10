def solution(players, callings):
    answer = []
    tmp = {player : i for i , player in enumerate(players)}
    
    for i in callings:
        now_rank = tmp[i]
        tmp[i] -= 1
        tmp[players[now_rank - 1]] += 1
        players[now_rank], players[now_rank - 1] = players[now_rank - 1], i
    # print(tmp)
    
    return players

solution(["mumu", "soe", "poe", "kai", "mine"]	, ["kai", "kai", "mine", "mine"])