﻿public class Solution {
    public string solution(string s) {
        string answer = "";
        if (s.Length % 2 == 0){
            answer += s[s.Length/2 - 1];
            answer += s[s.Length/2];
        }
        else {
            answer += s[s.Length/2];
        }
        
        
        return answer;
    }
}