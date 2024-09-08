using System;
using System.Collections.Generic;

public class Solution {
    public string[] solution(string my_string) {
        // string[] answer = new string[] {};
        List<string> aa = new List<string>();
        for (int i = 0; i < my_string.Length; i++){
            aa.Add(my_string.Substring(i,my_string.Length - i));
        }
        aa.Sort();
        
        
        return aa.ToArray();
    }
}