# https://school.programmers.co.kr/learn/courses/30/lessons/131130#


def opening(cards, i, box_table, open_, stack):
    if open_[i - 1] == 0:
        stack += 1
        open_[i - 1] = 1
        i = cards[i - 1]
        print(i, stack)
        opening(cards, i, box_table, open_, stack)
    else:
        box_table.append(stack)
        print("끝났쪙")
        return


def solution(cards):
    answer = 0
    box_table = []
    open_ = [0 for i in range(len(cards))]

    for i in range(len(cards)):
        stack = 0  # 어차피 한번 순회하면 버려야 함...
        opening(cards, i, box_table, open_, stack)

    box_table.sort(reverse=True)

    return box_table[0] * box_table[1]