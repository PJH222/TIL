using System;

public class Solution {
    public int solution(string[] order) {
        int answer = 0;
        foreach (string a in order){
            if (a.IndexOf("americano") != -1) answer += 4500;
            else if (a.IndexOf("latte") != -1) answer += 5000;
            else if (a.IndexOf("any") != -1) answer += 4500;
        }
        return answer;
    }
}