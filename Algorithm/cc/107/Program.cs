using System;
using System.Collections.Generic;

public class Solution {
    public int solution(string binomial) {
        int answer = 0;
        string[] aa = binomial.Split(' ');
        
        if (aa[1] == "+") return (int.Parse(aa[0]) + int.Parse(aa[2]));
        else if (aa[1] == "-") return (int.Parse(aa[0]) - int.Parse(aa[2]));
        else return (int.Parse(aa[0]) * int.Parse(aa[2]));
        return answer;
    }
}