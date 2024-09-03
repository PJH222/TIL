using System;

public class Solution {
    public int solution(string my_string) {
        int answer = 0;
        for (int i = 0; i < my_string.Length; i++){
            if (Char.IsDigit(my_string[i])){
                int a =  my_string[i];
                Console.WriteLine(answer);
                answer += a - 48;
            }
        }
        
        return answer;
    }
}

// 찬양하라... 갓 파이썬...