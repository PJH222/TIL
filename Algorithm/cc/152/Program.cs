using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int solution(string s) {
        int answer = 0;
        List<string> a = s.Split(" ").ToList();
        for (int i = 0 ; i<a.Count ; i++){
            if (a[i] == "Z"){
                answer -= int.Parse(a[i - 1]);
            }
            else {
                answer += int.Parse(a[i]);
            }
        }
        
        
        return answer;
    }
}