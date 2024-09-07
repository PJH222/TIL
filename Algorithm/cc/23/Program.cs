using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int[] solution(int n, int[] numlist) {
        // int[] answer = new int[] {};
        
        List<int> aa = new List<int>();
        
        for (int i = 0; i<numlist.Length; i++){
            if (numlist[i]%n == 0){
                aa.Add(numlist[i]);
            }
            
        }
        int[] answer = aa.ToArray();
        return answer;
    }
}