using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int[] solution(int[] array, int[,] commands) {
        List<int> answer = new List<int>();
        int cnt = 0;
        while (cnt < commands.GetLength(0)){
            List<int> tmp = new List<int>();
            for (int i = commands[cnt,0] - 1; i<=commands[cnt,1] - 1; i++){
                tmp.Add(array[i]);
                // Console.Write(array[i]);
            }
            tmp.Sort();
            // Console.WriteLine();
            answer.Add(tmp[commands[cnt,2] - 1]);
            cnt += 1;
            
        }
        
        return answer.ToArray();
    }
}