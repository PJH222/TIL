# https://school.programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words):
    answer = []
    people = {} #x-1 번째 사람마다 딕셔너리로 정리
    #이렇게 하는 이유는, 시간 제한에 걸릴일이 없기 때문에,,,
    #쓸데없이 개 복잡해지는거 같은데...?

    for i in range(n):
        people[i] = []

    for i in range(len(words)):
        #똑같은 단어를 말했을 떄 찾는 조건
        if  i > 0 and words[i-1][-1] == words[i][0]:
            people[(i)%n].append(words[i]) #인덱스 값임
            for j in range(n):
                if j != i%n and people[j].count(words[i]) != 0:
                    answer.append(i%n+1)
                    answer.append(people[i%n].index(words[i])+1)
                    return answer
        elif i == 0:
            people[(i) % n].append(words[i])  # 인덱스 값임

        elif words[i-1][-1] != words[i][0]:
            people[(i) % n].append(words[i])  # 인덱스 값임
            answer.append(i % n + 1)
            answer.append(people[i % n].index(words[i]) + 1)
            return answer
    return [0,0]


print(solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]	))
print(solution(5,["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]	))
print(solution(2,["hello", "one", "even", "never", "now", "world", "draw"]	))
print(solution(2,["hello", "one", "rven", "hello"]	))
#[1,2]
print(solution(2,["hello", "one", "even", "hello"]	))
# [2,2]