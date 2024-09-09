using System;

public class Solution {
    public int solution(string str1, string str2) {
        int answer = 0;
        if (str2.IndexOf(str1) != -1){
            return 1;
        }
        else{
            return 0;
        }
        
        return answer;
    }
}