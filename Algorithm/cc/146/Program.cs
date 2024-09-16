using System;
using System.Linq;
public class Solution {
    public string[] solution(string myStr) {
        string[] answer = new string[] {};
        myStr = myStr.Replace("a"," ");
        myStr = myStr.Replace("b"," ");
        myStr = myStr.Replace("c"," ");
        answer = myStr.Split(" ");
        answer = answer.Where(x => (x!="")).ToArray();
        
        string[] aa = new string[] {"EMPTY"};
        if (answer.Length == 0) return aa;
        return answer;
    }
}