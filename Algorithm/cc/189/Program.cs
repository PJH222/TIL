using System;

public class Solution {
    public int solution(int n) {
        int answer = 0;
        
        for (int i = 1 ; i <= n ; i++){
            for (int j = 0 ; j < 10000 ; j++){
                if (answer % 3 == 0) answer += 1;
                else if ((answer.ToString()).IndexOf("3") != -1) answer += 1;
                if (answer % 3 == 0) answer += 1;
                else if ((answer.ToString()).IndexOf("3") != -1) answer += 1;
                if (answer % 3 == 0) answer += 1;
                else if ((answer.ToString()).IndexOf("3") != -1) answer += 1;
                if (answer % 3 == 0) answer += 1;
                else if ((answer.ToString()).IndexOf("3") != -1) answer += 1;
            }

            answer += 1;
            Console.WriteLine(answer);
        }
        
        return answer - 1;
    }
}