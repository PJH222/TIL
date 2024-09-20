using System;
using System.Collections.Generic;

public class Solution {
    public int[] solution(int num, int total) {
        int[] answer = new int[] {};
        
        for (int i = -2000 ; i<=2000 ; i++){
            int tmp = 0;
            List<int> tmp_list = new List<int>();
            
            for (int j = i; j < i + num ; j++){
                tmp += j;
                tmp_list.Add(j);
            }
            
            // Console.WriteLine(tmp);
            
            if (tmp == total){
                answer = tmp_list.ToArray();
                // Console.WriteLine(answer);
            }
            
        }
        
        
        return answer;
    }
}