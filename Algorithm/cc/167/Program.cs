using System;

public class Solution {
    public int solution(string ineq, string eq, int n, int m) {
        int answer = 0;
        if ((ineq == "<") && (eq == "=")) if (n <= m) return 1;
        if ((ineq == ">") && (eq == "=")) if (n >= m) return 1;
        if ((ineq == "<") && (eq == "!")) if (n < m) return 1;
        if ((ineq == ">") && (eq == "!")) if (n > m) return 1;
        
        return answer;
    }
}