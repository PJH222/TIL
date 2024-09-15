using System;

public class Solution {
    public int solution(string myString, string pat) {
        int answer = 0;
        for (int i = 0; i<myString.Length - pat.Length  + 1; i++){
            if (myString.Substring(i,pat.Length) == pat){
                answer += 1;
            }
            Console.WriteLine(myString.Substring(i,pat.Length));
        }
        
        
        return answer;
    }
}