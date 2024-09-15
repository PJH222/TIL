using System;
using System.Collections.Generic;

public class Solution {
    public int[] solution(int[] arr, int[,] intervals) {
        List<int> answer = new List<int>();
        for (int i = intervals[0,0] ; i <= intervals[0,1] ; i++){
            answer.Add(arr[i]);
        }
        for (int i = intervals[1,0] ; i <= intervals[1,1] ; i++){
            answer.Add(arr[i]);
        }
        
        
        return answer.ToArray();
    }
}