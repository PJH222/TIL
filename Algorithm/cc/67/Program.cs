using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public string[] solution(string my_string) {
        // string[] answer = new string[] {};
        string[] aa = my_string.Split();        
        List<string> answer = new List<string>();
        for (int i = 0 ; i < aa.Length; i++){
            if (aa[i] != ""){
                answer.Add(aa[i]);
            }
        }
        
        
        return answer.ToArray();
    }
}