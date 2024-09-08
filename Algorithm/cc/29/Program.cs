using System;
using System.Collections.Generic;

public class Solution {
    public int[] solution(int start_num, int end_num) {
        // int[] answer = new int[] {};
        List<int> aa = new List<int>();
        
        for (int i=end_num; i<= start_num; i++){
            aa.Add(i);
        }
        int[] answer = aa.ToArray();
        Array.Reverse(answer);
        return answer;
    }
}