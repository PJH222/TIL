import sys
sys.stdin = open('./input.txt')

# 근데 이건 2 묶음씩 나누는 것 아닌가...?
def divide(first_number,last_number):
    if first_number == last_number:
        return first_number

    first_v = divide(first_number,(first_number+last_number)//2)
    second_v = divide((first_number+last_number)//2+1, last_number)

    if cards[first_v] == cards[second_v]:
        return first_v if first_v < second_v else second_v
    elif abs(cards[first_v]-cards[second_v]) == 2:
        return first_v if cards[first_v] < cards[second_v] else second_v
    elif abs(cards[first_v]-cards[second_v]) == 1:
        return second_v if cards[first_v] < cards[second_v] else first_v

T = int(input())
for t in range(T):
    N = int(input())
    cards = list(map(int,input().split()))
    new_list = []
    print('#{} {}'.format(t+1,divide(0,N-1)+1))