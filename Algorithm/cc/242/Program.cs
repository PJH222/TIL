using System;

public class Solution {
    public string solution(string s) {
        string answer = "";
        foreach (string str in s.Split(" ")){
            for (int i=0; i<str.Length ;i++){
                if (i%2 == 0) answer += str[i].ToString().ToUpper();
                else answer += str[i].ToString().ToLower();
            }
            if (answer.Length != s.Length) answer += " ";
        }
        
        return answer;
    }
}