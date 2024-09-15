using System;
using System.Linq;
using System.Collections.Generic;

public class Solution {
    public string solution(string my_string, int[] indices) {
        string answer = "";
        List<int> aa = indices.ToList();
        
        for (int i = 0 ; i<my_string.Length; i++){
            if (Array.IndexOf(indices,i) ==  -1){
                answer += my_string[i];
            }
        }
        
        return answer;
    }
}