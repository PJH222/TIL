using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public string[] solution(string[] quiz) {
        string[] answer = new string[quiz.Length];
        for (int i = 0 ; i < quiz.Length ; i++){
            List<string> a = quiz[i].Split(" ").ToList();
            
            
                int x1 = int.Parse(a[0].ToString());
                int x2 = int.Parse(a[2].ToString());
                int x3 = int.Parse(a[4].ToString());
                
                string c1 = a[1];
                
                if ((c1 == "+") && (x1 + x2 == x3)){
                    answer[i] = "O";
                }
                else if ((c1 == "-") && (x1 - x2 == x3)){
                    answer[i] = "O";
                } 
                else {
                    answer[i] = "X";
                }
                
            
        }
        
        
        return answer;
    }
}