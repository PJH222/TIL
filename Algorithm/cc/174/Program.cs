using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int[] solution(int[] arr, int k) {
        int[] answer = arr.Distinct().ToArray();
        List<int> result = new List<int>();
        
        for (int i = 0; i < k ; i++){
            int a = i < answer.Length ? answer[i] : -1 ;
            result.Add(a);
            
        }
        
        return result.ToArray();
    }
}