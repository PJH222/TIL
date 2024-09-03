using System;

public class Solution {
    public int solution(int n) {
        int answer = 0;
        
        for (int i = 1; i<=100; i++){
            if (i * 7 >= n){
                return i;
            }
        }
        
        return answer;
    }
}