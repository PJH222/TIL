using System;
using System.Collections.Generic;

public class Solution {
    public int solution(int n) {
        int answer = 0;
        string a = n.ToString();
        List<char> b = new List<char>(a);
        foreach (char c in b){
            answer += int.Parse(c.ToString());
        }
        
        return answer;
    }
}