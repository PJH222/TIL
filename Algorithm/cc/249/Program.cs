using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int[] solution(int[] numbers) {
        List<int> answer = new List<int>();
        for(int i = 0; i<numbers.Length ;i++){
            for (int j = i+1; j<numbers.Length ;j++){
                if (answer.IndexOf(numbers[i] + numbers[j])==-1) answer.Add(numbers[i] + numbers[j]);
            }
        }
        
        answer.Sort();
        return answer.ToArray();
    }
}