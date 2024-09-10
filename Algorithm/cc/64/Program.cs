using System;

public class Solution {
    public int solution(string myString, string pat) {
        int answer = 0;
        string aa = "";
        foreach (char c in myString) {
            if (c == 'A'){
                aa += 'B';
            }
            else{
                aa += 'A';
            }
        }
        
        if (aa.IndexOf(pat) != -1) {
            return 1;
        }
        
        return answer;
    }
}