using System;

public class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        foreach (int a in num_list){
            int b = a;
            while (true) {
                if (b != 1){
                    if (b%2 == 0) {
                        b = b/2;
                        answer += 1;
                    }
                    else {
                        b -= 1;
                        b = b/2;
                        answer += 1;
                    }
                }
                else if (b == 1) {
                    break;
                }
            }
        }
        
        return answer;
    }
}