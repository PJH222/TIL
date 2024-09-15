using System;

public class Solution {
    public string solution(string my_string) {
        string answer = "";
        for (int i = 0 ; i<my_string.Length ; i++) if (answer.IndexOf(my_string[i]) == -1) answer += my_string[i];
        return answer;
    }
}