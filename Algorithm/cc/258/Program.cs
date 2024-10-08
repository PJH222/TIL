using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int solution(int k, int m, int[] score) {
        int answer = 0;
        List<int> result = score.ToList();
        result = result.OrderByDescending(x => x).ToList();
        
        List<int> tmp = new List<int>();
        
        for (int i=0 ; i<result.Count ; i++ ){
            tmp.Add(result[i]);
            if (tmp.Count == m){
                answer += tmp.Min() * m;
                tmp.Clear();
            }
        }
        
        return answer;
    }
}