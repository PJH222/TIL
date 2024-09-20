using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int solution(int[] rank, bool[] attendance) {
        int answer = 0;
        List<int> tmp = new List<int>();
        int rankk = 1;
        for (int repeat = 0; repeat < rank.Length ; repeat ++){
            for (int j = 0; j < rank.Length ; j ++){
                if ((rank[j] == rankk) && (attendance[j] == true)) {
                    tmp.Add(j);
                    rankk += 1;
                }
                else if ((rank[j] == rankk) && (attendance[j] != true)) {
                    rankk += 1;
                }
            }
            if (tmp.Count == 3) break;
        }
        foreach (int t in tmp){
            Console.WriteLine(t);
        }
        answer = tmp[0] * 10000 + tmp[1] * 100 + tmp[2];
        return answer;
    }
}