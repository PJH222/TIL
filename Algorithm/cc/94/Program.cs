using System;

public class Solution {
    public int solution(string str1, string str2) {
        if (str1.IndexOf(str2) != -1){
            return 1;
        }
        return 2;
    }
}