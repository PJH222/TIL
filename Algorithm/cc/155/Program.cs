using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int[] solution(int n) {
        List<int> answer = new List<int>();
        int cnt = 2;
        while (n != 1) {
            if (n%cnt == 0){
                n /= cnt;
                if (answer.IndexOf(cnt) == -1){
                    answer.Add(cnt);
                }
            }
            
            else {
                cnt += 1;
            }
        }
        
        return answer.ToArray();
    }
}