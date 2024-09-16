using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int solution(int[] array, int n) {
        int answer = 0;
        int sm = 100;
        List<int> aa = array.ToList();
        aa.Sort();
        List<int> bb = new List<int>();
        for (int i = 0 ; i < array.Length ; i++){
            bb.Add(Math.Abs(aa[i] - n));
        }
        
        for (int i = 0 ; i < array.Length ; i++){
            if (bb[i] < sm) {
                sm = bb[i];
                answer = aa[i];
            }
        }
        
        return answer;
    }
}