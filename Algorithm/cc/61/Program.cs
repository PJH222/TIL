using System;
using System.Diagnostics;

public class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        if ((a%2 == 0) && (b%2 == 0)){
            return Math.Abs(a - b);
        }
        else if ((a%2 == 1) && (b%2 == 1)){
            return a*a + b*b;
        }
        else{
            return 2 * (a+b);
        }
        
        return answer;
    }
}