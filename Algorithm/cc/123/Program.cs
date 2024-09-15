using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public string[] solution(string myString) {
        List<string> answer = (myString.Split("x")).ToList();
        int cnt = 0;
        for (int i = 0 ; i<answer.Count ; i++){ if (answer[i]=="") cnt += 1;}
        for (int i = 0 ; i<cnt ; i++) answer.Remove("");
        
        answer.Sort();
        return answer.ToArray();
    }
}