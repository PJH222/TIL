using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public string[] solution(string[] strArr) {
        List<string> answer = new List<string>();
        for (int i=0 ; i < strArr.Length; i++ ){
            if (i%2 == 0){
                answer.Add(strArr[i].ToLower());
            }
            else {
                answer.Add(strArr[i].ToUpper());
            }
        }   
        return answer.ToArray();
    }
}