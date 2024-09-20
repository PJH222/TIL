using System;

public class Solution {
    public int[] solution(int numer1, int denom1, int numer2, int denom2) {
        int[] answer = new int[2] {0,0};
        int a = denom1 * denom2;
        int b = numer1 * denom2 + numer2 * denom1;
        for (int i = 2 ; i<Math.Max(a,b) ; i++){
            for (int j = 0 ; j < 10 ; j++){
                if ((a%i == 0)&&(b%i == 0)){
                    a /= i;
                    b /= i;
                }
            }
        }
        answer[0] = b;
        answer[1] = a;
        
        return answer;
    }
}