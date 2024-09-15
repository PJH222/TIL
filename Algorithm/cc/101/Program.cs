using System;
using System.Collections.Generic;

public class Solution {
    public int[] solution(string my_string) {
        List<int> answer = new List<int>();
        for (int i = 0 ; i < my_string.Length ; i ++){
            if (char.IsNumber(my_string[i]) == true){
                answer.Add(my_string[i] - 48);
            }
        }
        answer.Sort();
        return answer.ToArray();
    }
}