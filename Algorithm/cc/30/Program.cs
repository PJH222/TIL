using System;
using System.Collections.Generic;

public class Solution {
    public int[] solution(int n, int k) {
        // int[] answer = new int[] {};
        List<int> aa = new List<int>();
        for (int i = 1; i <= n; i++){
            if (i%k == 0){
                aa.Add(i);
            }
        }
        
        int[] answer = aa.ToArray();
        
        return answer;
    }
}