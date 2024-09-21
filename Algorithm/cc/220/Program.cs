using System;

public class Solution {
    public long solution(long a, long b) {
        long answer = 0;
        if (a == b) {
            answer += a;
            return answer;
        }
        
        long maxx = a > b ? a : b;
        long minn = a > b ? b : a;
        
        return (maxx + minn) * (maxx - minn + 1) / 2;
    }
}