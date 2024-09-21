using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public string solution(string s) {
        string answer = "";
        List<char> a = new List<char>();
        foreach(char c in s){
            a.Add(c);
        }
        a.Sort();
        a.Reverse();
        
        return string.Join("",a);
    }
}