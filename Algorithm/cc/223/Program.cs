using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int solution(long num) {
        int answer = 0;
        int cnt = 0;
        if (num == 1) return 0;
        
        while (cnt < 500) {
            if (num == 1) break; 
            if (num % 2 == 0){
                num /= 2;
                cnt += 1;
                continue;
            }
            else {
                num = num * 3 + 1;
                cnt += 1;
                continue;
            }
        }
        if (num == 1) return cnt;
        else return -1;
        
        
    }
}