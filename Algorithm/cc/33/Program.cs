using System;

public class Solution {
    public int solution(string my_string, string is_suffix) {
        int answer = 0;
        for (int i=0; i <= my_string.Length; i++){
            if (my_string.Substring(my_string.Length - i) == is_suffix){
                return 1;
            }
        }
        
        return answer;
    }
}