using System;
using System.Collections.Generic;
using System.Linq;
// using System.Range;

public class Solution {
    public int[] solution(int[] num_list) {
        // int[] answer = new int[]{};
        List<int> aa = num_list.ToList();
        aa.Sort();
        
        int[] bb = aa.ToArray();
        
        // var cc = bb.Take(num_list.Length - 5);
        
        List<int> answer = new List<int>();
        for (int i = 5 ; i<bb.Length; i++){
            answer.Add(bb[i]);
        }
        
        return answer.ToArray();
    }
}