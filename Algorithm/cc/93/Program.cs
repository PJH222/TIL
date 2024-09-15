using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int solution(int[] numbers) {
        
        List<int> aa = numbers.ToList();
        aa.Sort();
        
        int answer = aa[numbers.Length - 1] * aa[numbers.Length - 2];
        
        return answer;
    }
}