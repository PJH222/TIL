using System;
using System.Collections.Generic;

public class Solution {
    public int[] solution(int n) {
        List<int> oddNumbers = new List<int>();
        
        for (int i = 1; i <= n; i += 2) {
            oddNumbers.Add(i);
        }
        
        return oddNumbers.ToArray();
    }
}
