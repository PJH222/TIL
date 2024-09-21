using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public long solution(long n) {
        string answer = "";
        string a = n.ToString();
        List<char> b = new List<char>(a);
        b.Sort();
        b.Reverse();  
        string c = string.Join("",b);
        return long.Parse(c);
    }
}