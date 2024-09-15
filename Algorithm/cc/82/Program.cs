using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int[] solution(int[] num_list, int n) {
        
        List<int> front = new List<int>();
        List<int> back = new List<int>();
        for (int i = 0 ; i<num_list.Length ; i ++){
            if ( i < n ) {
                front.Add(num_list[i]);
            }
            else {
                back.Add(num_list[i]);
            }
        }
        List<int> answer = back.Concat(front).ToList();
        return answer.ToArray();
    }
}