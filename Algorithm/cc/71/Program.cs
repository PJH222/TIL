using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public string[] solution(string[] names) {
        // string[] answer = new string[] {};
        List<string> answer = new List<string>();
        for (int i = 0 ; i < names.Length ; i += 5){
            answer.Add(names[i]);
        }
        
        return answer.ToArray();
    }
}