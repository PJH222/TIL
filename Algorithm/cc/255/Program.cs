using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int solution(int number, int limit, int power) {
        int answer = 0;
        List<int> result = new List<int>();        
        for (int i = 1; i<=number ;i++){
            int tmp = 0;
            for (int j=1; j<(int)Math.Sqrt(i) + 1 ;j++){
                if (i%j == 0) {
                    tmp += 1;
                    if (Math.Pow(j,2) != i){
                        tmp +=1;    
                    }
                    
                }
            }
            if (tmp <= limit) answer += tmp;
            else answer += power;
        }
        
        return answer;
    }
}