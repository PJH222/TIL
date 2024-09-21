using System;
using System.Collections.Generic;

public class Solution {
    public int[] solution(int[] arr, int divisor) {
        List<int> answer = new List<int>();
        foreach (int i in arr){
            if (i%divisor == 0){
                answer.Add(i);
            }
        }
        answer.Sort();
        if (answer.Count == 0){
            answer.Add(-1);
        }
        return answer.ToArray();
    }
}