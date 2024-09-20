using System;

public class Solution {
    public string solution(string code) {
        string answer = "";
        int mode = 0;
        string tmp1 = "01";
        string word = "";
        for (int i = 0 ; i<code.Length ; i++){
            if ((tmp1.IndexOf(code[i]) == -1) && (mode == 0) && (i%2 == 0)) {
                word += code[i];
            }
            else if ((tmp1.IndexOf(code[i]) == -1) && (mode == 1) && (i%2 == 1)) {
                word += code[i];
            }
            else if ((mode == 0) && (code[i] == '1')) mode = 1;
            else if ((mode == 1) && (code[i] == '1')) mode = 0;
            
        }
        if (word.Length == 0) return "EMPTY";
        
        return word;
    }
}