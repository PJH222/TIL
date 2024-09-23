using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int[] solution(int k, int[] score) {
        List<int> answer = new List<int>();
        List<int> ranking = new List<int>();
        for (int i = 0; i<score.Length ;i++){
            if (ranking.Count < k) {
                ranking.Add(score[i]);
                ranking = ranking.OrderByDescending(x=>x).ToList();
                answer.Add(ranking[i]);
            }
            else {
                ranking.Add(score[i]);
                ranking = ranking.OrderByDescending(x=>x).ToList();
                ranking.RemoveAt(k);
                answer.Add(ranking[k - 1]);
            }Console.WriteLine();
            // foreach(int j in ranking) Console.WriteLine(j);
        }
        
        return answer.ToArray();
    }
}