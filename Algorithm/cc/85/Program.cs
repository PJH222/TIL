using System;
using System.Collections.Generic;

public class Solution {
    public int[] solution(int[] arr) {
        List<int> answer = new List<int>();
        
        for (int i = 0 ; i < arr.Length ; i++){
            if ((arr[i] >= 50) && (arr[i]%2 == 0)){
                answer.Add(arr[i]/2);
            }
            else if ((arr[i] < 50) && (arr[i]%2 != 0)){
                answer.Add(arr[i]*2);
            }
            else{
                answer.Add(arr[i]);
            }
        }
        
        return answer.ToArray();
    }
}