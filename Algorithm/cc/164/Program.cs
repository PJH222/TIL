using System;

public class Solution {
    public int solution(string my_string) {
        
        string[] a = my_string.Split(" ");
        int answer = int.Parse(a[0]);
        for (int i = 1; i<my_string.Split(" ").Length - 1; i++){
            if (a[i] == "+"){
                answer += int.Parse(a[i+1]);
            }
            else if (a[i] == "-"){
                answer -= int.Parse(a[i+1]);
            }
        }
        return answer;
    }
}