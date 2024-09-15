using System;

public class Solution {
    public int solution(int a, int b, bool flag) {
        int answer = 0;
        if (flag == true) return a + b;
        return a - b;
    }
}