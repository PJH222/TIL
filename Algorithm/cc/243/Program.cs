using System;

public class Solution {
    public int solution(int[] number) {
        int answer = 0;
        for (long i = 0; i<number.Length ;i++){
            for (long j=i+1; j<number.Length; j++){
                for(long k=j+1; k<number.Length; k++){
                    if (number[i] + number[j] + number[k] == 0) answer += 1;
                }
            }
        }
        
        return answer;
    }
}