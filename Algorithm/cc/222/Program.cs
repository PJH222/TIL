using System;

public class Solution {
    public string solution(string[] seoul) {
        string answer = "";
        int a = Array.IndexOf(seoul, "Kim");
        answer = "김서방은 " + a.ToString() +"에 있다";
        return answer;
    }
}