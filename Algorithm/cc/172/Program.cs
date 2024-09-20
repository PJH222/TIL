using System;

public class Solution {
    public ulong solution(int balls, int share) {
        int k = Math.Min(share, balls - share);
        ulong result = 1;

        for (int i = 0; i < k; i++) {
            result *= (ulong)(balls - i);  
            result /= (ulong)(i + 1);
        }

        return result;
    }
}


// 넘 어려웡....
