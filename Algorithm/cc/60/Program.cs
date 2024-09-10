using System;

public class Solution {
    public int solution(string num_str) {
        int answer = 0;
        foreach (char c in num_str){
            answer += int.Parse((c.ToString()));
        }
        return answer;
    }
}