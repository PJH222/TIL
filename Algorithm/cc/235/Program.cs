using System;

public class Solution {
    public bool solution(string s) {
        bool answer = false;
        if (((s.Length == 4) || (s.Length == 6))) {
            foreach (char c in s){
                if (!Char.IsNumber(c))
                    return false;
            }
            
            return true;
        }
        
        
        return answer;
    }
}