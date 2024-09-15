using System;
using System.Collections.Generic;

public class Solution {
    public string solution(string my_string) {
        string answer = (my_string.ToLower());
        List<char> aa = new List<char>();
        for (int i = 0 ; i < my_string.Length ; i ++){
            aa.Add(answer[i]);
        }
        aa.Sort();
        return string.Join("",aa);
    }
}