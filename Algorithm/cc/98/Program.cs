﻿using System;

public class Solution {
    public int[] solution(int[] num_list) {
        int[] answer = new int[] {0, 0};
        for (int i = 0 ; i < num_list.Length ; i++){
            if (num_list[i]%2 == 1){
                answer[1] += 1;
            }
            else{
                answer[0] += 1;
            }
        }
        
        return answer;
    }
}