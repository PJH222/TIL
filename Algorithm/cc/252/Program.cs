using System;

public class Solution {
    public int solution(int a, int b, int n) {
        int answer = 0;
        while (n > a - 1) {
            n -= a;
            n += b;
            answer += b;
        }
        
        
        return answer;
    }
}