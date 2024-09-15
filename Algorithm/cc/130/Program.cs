using System;
using System.Collections.Generic;

public class Solution {
    public int[] solution(string[] intStrs, int k, int s, int l) {
        List<int> answer = new List<int>();        
        foreach (string a in intStrs){
            if (int.Parse(a.Substring(s,l)) > k ) 
                answer.Add(int.Parse(a.Substring(s,l)));
                           
        }
        return answer.ToArray();
    }
}