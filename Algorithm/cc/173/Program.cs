using System;
using System.Linq;

public class Solution {
    public int solution(int[] sides) {
        int answer = 0;
        // 추가하는 변이 가장 긴 변일 경우
        // 추가하는 변이 가장 긴 변 보다 작은 경우
        
        int a = sides.Sum();
        
        for (int i = sides.Max() ; i < a ; i++){
            answer += 1;
        }
        
        for (int i = 1 ; i < sides.Max() ; i++){
            if (sides.Min() + i > sides.Max()) answer += 1;
        }
        
        
        
        return answer;
    }
}   