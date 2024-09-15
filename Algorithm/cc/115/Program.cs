using System;

public class Solution {
    public string solution(int age) {
        string answer = "";
        string a = age.ToString();
        string b = "abcdefghij";
        foreach (char c in a){
            answer += b[Int32.Parse(c.ToString())];
        }
        return answer;
    }
}