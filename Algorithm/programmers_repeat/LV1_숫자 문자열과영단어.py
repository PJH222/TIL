def solution(s):
    answer = ''
    s = list(s)
    nums_list = ['zero','one','two','three','four','five','six','seven','eight','nine']

    while s:
        if s[0].isdigit():
            answer += s[0]
            del s[0]

        else:
            for i in nums_list:
                # print("".join(s[:3]))
                if "".join(s[:3]) == i:
                    bb = nums_list.index(i)
                    answer += str(bb)
                    del s[:3]

                elif "".join(s[:4]) == i:
                    bb = nums_list.index(i)
                    answer += str(bb)
                    del s[:4]

                elif "".join(s[:5]) == i:
                    bb = nums_list.index(i)
                    answer += str(bb)
                    del s[:5]

        # print(s)
    answer = int(answer)
    print(answer)

    return answer

solution("one4seveneight"	)
solution("23four5six7")
solution("2three45sixseven"	)
solution("123"	)

