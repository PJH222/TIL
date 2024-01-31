# 최대 10만 개의 경우
# 대소문자, 숫자를 바꿔서 같은지 아닌지 확인하는 것은 안됨..
# 있는그대로 비교할 수 있는 방법이 있을까?




def solution(files):
    answer = [[] for i in range(len(files))]
    return answer




print(solution( ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
# 출력: ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]

print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))
# 출력: ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]

