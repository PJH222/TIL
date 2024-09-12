using System;
using System.Collections.Generic;

public class Solution {
    public int[] solution(int n) {
        List<int> aa = new List<int>();
        int b = 2;
        while (b != 1){
            aa.Add(n);
            if (n%2 == 0){
                n = n / 2;
            }
            else {
                n = n * 3 + 1;
            }
            b = n;
        }
        aa.Add(1);
        return aa.ToArray();
    }
}