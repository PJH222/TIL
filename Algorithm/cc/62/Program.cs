using System;
using System.Linq;
using System.Collections.Generic;

public class Solution {
    public int[] solution(int[] num_list) {
        List<int> aa = (num_list.ToList());
        List<int> answer = new List<int>();
        
        aa.Sort();
        
        for (int i = 0; i < 5 ; i++){
            answer.Add(aa[i]);
        }
        
        
        
        return answer.ToArray();
    }
}