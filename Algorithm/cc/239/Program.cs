using System;
using System.Linq;
using System.Collections.Generic;

public class Solution {
    public int solution(int[] d, int budget) {
        int answer = 0;
        int result = 0;
        List<int> a = new List<int>(d);
        a.Sort();
        foreach (int i in a){
            if (result + i > budget){
                return answer;
            }
            else {
                result += i;
                answer += 1;
            }
        }
        
        
        return answer;
    }
}