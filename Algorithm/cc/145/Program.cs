using System;

public class Solution {
    public int[] solution(int[] arr, int[,] queries) {
        int[] answer = new int[] {};
        for (int i = 0 ; i < queries.GetLength(0) ; i++){
            int a = queries[i,0];
            int b = queries[i,1];
            int tmp = arr[b];
            
            arr[b] = arr[a];
            arr[a] = tmp;
        }
        
        return arr;
    }
}