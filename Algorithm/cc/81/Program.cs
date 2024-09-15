using System;
using System.Collections.Generic;

public class Solution {
    public string[] solution(string[] strArr) {
        List<string> answer = new List<string>();
        
        for (int i = 0; i < strArr.Length ; i ++){
            if ((strArr[i]).IndexOf("ad") == -1){
                answer.Add(strArr[i]);
            }
        }
        return answer.ToArray();
    }
}