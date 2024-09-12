using System;

public class Solution {
    public string solution(string my_string, string alp) {
        // char a = Char.ToUpper(alp);
        string answer = my_string.Replace(alp,alp.ToUpper());
        return answer;
    }
}