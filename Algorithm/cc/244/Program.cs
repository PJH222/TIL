using System;
using System.Collections.Generic;
using System.Linq;


public class Solution {
    public int solution(int[,] sizes) {
        int answer = 0;
        List<int> a = new List<int>(); // 긴쪽
        List<int> b = new List<int>(); // 짧은 쪽
        
        for (int i = 0 ;i<sizes.GetLength(0) ; i++){
            int minn = Math.Min(sizes[i,0] , sizes[i,1]);
            int maxx = Math.Max(sizes[i,0] , sizes[i,1]);
            a.Add(maxx);
            b.Add(minn);
        }
        
        return a.Max() * b.Max();
    }
}