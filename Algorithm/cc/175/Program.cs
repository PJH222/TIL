using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int[] solution(int[] arr, int[,] queries) {
        List<int> answer = new List<int>();
        
        for (int i = 0 ; i < queries.GetLength(0) ; i++){
            List<int> tmp = arr.Skip(queries[i,0]).Take(queries[i,1] - queries[i,0] + 1).ToList();
            int minn = 1000000;
            foreach (int a in tmp) {
                if ((a > queries[i,2]) && (a < minn)) minn = a;
            }
            if (minn != 1000000) answer.Add(minn);
            else answer.Add(-1);
        }
        
        return answer.ToArray();
    }
}