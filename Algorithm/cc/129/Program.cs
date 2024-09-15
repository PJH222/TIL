using System;

public class Solution {
    public string solution(string my_string, int s, int e) {
        string answer = "";
        for (int i = 0 ; i<s ; i++){
            answer += my_string[i];
        }
        for (int i = e ; i >= s ; i--){
            answer += my_string[i];
        }
        for (int i = e + 1 ; i<my_string.Length ; i++){
            answer += my_string[i];
        }
        
        return answer;
    }
}