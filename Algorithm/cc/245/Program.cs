using System;

public class Solution {
    public string solution(string s, int n) {
        string answer = "";
        string a = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz";
        string b = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ";
        
        foreach (char c in s){
            if ((c != ' ')&&(a.IndexOf(c) != -1)){
                answer += a[a.IndexOf(c) + n].ToString();
            }
            else if ((c != ' ')&&(b.IndexOf(c)!=-1)){
                answer += b[b.IndexOf(c) + n].ToString();
            }
            else {
                answer +=  " ";
            }
        }
        return answer;
    }
}