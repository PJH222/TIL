using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int[] solution(int[,] score) {
        List<int> result = new List<int>();
        int[] answer = Enumerable.Repeat(1, score.GetLength(0)).ToArray();
        
        for (int i = 0 ; i<score.GetLength(0) ; i++){
            int tmp = 0;
            for (int j = 0 ; j < 2 ; j++){
                tmp += score[i,j];
            }
            result.Add(tmp);
        }
        
        for (int i = 0 ; i<result.Count ; i++){
            for (int j = 0 ; j<result.Count ; j++){
                if (result[i] > result[j]) answer[j] += 1;
            }   
        }
        
        
        return answer;
    }
}