using System;
using System.Collections.Generic;

public class Solution {
    public int solution(int a, int d, bool[] included) {
        int answer = 0;
        // List<int> aa = new List<int>();
        int aa = a;
        
        for (int i = 0 ; i<included.Length ; i ++){
            if (included[i] == true) answer += aa;
            aa += d;
            
        }
        return answer;
    }
}