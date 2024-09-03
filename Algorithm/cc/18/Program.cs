using System;

public class Solution {
    public int solution(int hp) {
        int answer = 0;
    
        int aa = 0;
        int bb = 0;
        int cc = 0;
        
        answer += hp / 5;
        aa = hp / 5;
        
        hp -= aa * 5;
        
        answer += hp / 3;
        bb = hp / 3;
        
        hp -= bb * 3;
        
        answer += hp / 1;
      
        
        
        return answer;
    }
}