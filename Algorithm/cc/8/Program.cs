using System;

public class Solution {
    public int solution(int n) {
        int answer = 0;
        for (int i = 0; i < 1000001; i++){
            if (i * i == n)
                return 1;
        }
        
        return 2;
    }
}

// 최적화 따위는 개나 줘버린;