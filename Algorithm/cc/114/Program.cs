using System;

public class Solution {
    public int solution(int n) {
        int answer = 1;
        
        while (true) {
            if (answer * 6 % n == 0){
                return answer;
            }
            else {
                answer += 1;
            }
        }
        
        return answer;
    }
}