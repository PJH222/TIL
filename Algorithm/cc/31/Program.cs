using System;

public class Solution {
    public int solution(string my_string, string is_prefix) {
        int answer = 0;
        string aa = (my_string.IndexOf(is_prefix).ToString());
        Console.WriteLine(aa);
        if (aa == "0"){
            return 1;
        }
        
        return 0;
    }
}