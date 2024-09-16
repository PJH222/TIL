using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int[] solution(int[] arr, int[,] queries) {
        for (int i = 0 ; i < queries.GetLength(0) ; i++){
            int a = queries[i,0];
            int b = queries[i,1];
            // Console.WriteLine(a);
            for (int j = a; j<=b ; j++){
                arr[j] += 1;
            }
        }
        return arr;
    }
}