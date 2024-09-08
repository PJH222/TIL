using System;
using System.Collections.Generic;
using System.Linq;
public class Solution {
    public int[] solution(int[] num_list) {
        int[] answer = new int[num_list.Length + 1];
        
        int b = num_list[num_list.Length - 1];
        int c = num_list[num_list.Length - 2];
        
        if (b > c){
            answer[answer.Length - 1] = b - c;
        }
        else{
            answer[answer.Length - 1] = b * 2;
        }
        
        for (int i=0; i<answer.Length - 1; i++){
            answer[i] = num_list[i];
        }
        
        return answer;
    }
}