using System;

public class Solution {
    public int solution(string myString, string pat) {
        int answer = 0;
        if ((myString.ToUpper()).IndexOf(pat.ToUpper()) != -1){
            return 1;
        }
        
        return answer;
    }
}