using System;

public class Solution {
    public int solution(int a, int b) {
        int answer = 2;
        for (int i = 1 ; i < 1001 ; i++){
            for (int j =0 ; j<10; j++) {
                if ((a%i == 0 )&&(b%i == 0)) {
                    a /= i;
                    b /= i;
                }
            }
        }
        for (int i = 2; i < 6 ; i += 3){
            for (int j = 0 ; j < 10 ; j++){
                if (b%i == 0) b/=i;
            }
        }
        
        if (b==1) return 1;
        
        return answer;
    }
}