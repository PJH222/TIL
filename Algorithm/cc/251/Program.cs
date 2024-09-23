using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public string[] solution(string[] strings, int n) {
        string[] answer = new string[] {};
        string[] a = strings.OrderBy(x => x).OrderBy(x => x[n]).ToArray();   
        return a;
    }
}