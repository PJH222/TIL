using System;

public class Solution {
    public int solution(int n, string control) {
        int answer = n;
        for (int i = 0; i<control.Length; i++){
            string a = control.Substring(i,1);
            if (a == "w"){
                answer += 1;
            }
            else if (a == "s"){
                answer -= 1;
            }
            else if (a == "d"){
                answer += 10;
            }
            else if (a == "a"){
                answer -= 10;
            }
            // Console.WriteLine(a);
        }
        return answer;
    }
}