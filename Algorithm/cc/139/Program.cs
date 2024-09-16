using System;

public class Solution {
    public int solution(int n) {
        int answer = 1;
        int tmp = 1;
        while (true){
            if (tmp * answer < n) {
                tmp *= answer;
                answer += 1;
            }
            else if (tmp * answer== n){
                return answer;
            }
            else return answer - 1;
        }
        return answer;
    }
}