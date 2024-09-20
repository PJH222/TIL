using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int[,] solution(int[,] arr) {
        int maxx = Math.Max(arr.GetLength(1),arr.GetLength(0));
        int[,] answer = new int[maxx,maxx];
        
        for (int i = 0; i<arr.GetLength(0) ; i++){
            for (int j = 0 ; j<arr.GetLength(1); j++){
                answer[i,j] = arr[i,j];
            }
        }
        
        return answer;
    }
}