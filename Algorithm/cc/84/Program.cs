using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public string solution(string myString) {
        List<char> answer = new List<char>();
        for (int i = 0; i < myString.Length ; i ++) {
            answer.Add(char.ToUpper(myString[i]));
        }
        
        return string.Join("",answer);
    }
}