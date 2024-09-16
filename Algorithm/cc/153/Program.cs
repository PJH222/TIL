using System;

public class Solution {
    public string solution(int q, int r, string code) {
        string answer = "";
        for (int i = 0 ; i<code.Length ; i ++){
            if (i%q == r) answer += code[i];
        }
        
        
        return answer;
    }
}