using System;
using System.Collections.Generic;

public class Solution {
    public int[] solution(int[] num_list, int n) {
        // int[] answer = new int[] {};
        
        List<int> aa = new List<int>();
        for (int i = n - 1; i < num_list.Length; i++){
            aa.Add(num_list[i]);
        }
        int[] answer = aa.ToArray();
        
        return answer;
    }
}