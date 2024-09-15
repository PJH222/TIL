using System;
using System.Linq;
using System.Collections.Generic;

public class Solution {
    public int[] solution(int[] arr, bool[] flag) {
        List<int> answer = new List<int>();
        for (int i = 0; i<flag.Length ; i ++){
            if (flag[i] == true) {
                for (int j = 0 ; j < arr[i]*2 ; j++){
                    answer.Add(arr[i]);
                }
                
            }
            else {
                for (int j = 0 ; j < arr[i] ; j++){
                    answer.RemoveAt(answer.Count - 1);
                }
            }
        }
        
        
        return answer.ToArray();
    }
}