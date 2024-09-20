using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public string[] solution(string[] picture, int k) {
        List<string> answer = new List<string>();
        for (int i = 0 ; i<picture.Length ; i++){
            string tmp1 = "";
            foreach (char c in picture[i]){
                for (int j = 0 ; j < k ; j++){
                    tmp1 += c;
                }
            }
            for (int l = 0 ; l < k ; l++){
                answer.Add(tmp1);    
            }
            
            
            
        }
        
        
        return answer.ToArray();
    }
}