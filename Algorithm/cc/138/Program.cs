using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int[] solution(int[] emergency) {
        List<int> answer = new List<int>();
        List<int> aa = emergency.ToList();
        aa.Sort();
        aa = Enumerable.Reverse(aa).ToList();
        foreach (int a in emergency){
            answer.Add(aa.IndexOf(a) + 1);
        }
        return answer.ToArray();
    }
}