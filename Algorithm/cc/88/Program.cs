using System;
using System.Collections.Generic;

public class Solution {
    public int[] solution(string[] strlist) {
        List<int> answer = new List<int>();
        
        for (int i = 0 ; i<strlist.Length ; i++){
            answer.Add(strlist[i].Length);
        }
        return answer.ToArray();
    }
}