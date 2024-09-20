using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int solution(int[,] lines) {
        int answer = 0;
        List<string> a = new List<string>();
        
        for (int i = 0; i<3 ; i++){
            for (int j = lines[i,0]; j<lines[i,1] ;j++){
                string b = "";
                b += j.ToString();
                b += (j+1).ToString();
                if (a.Where(x => x== b).Count() == 2) continue;
                a.Add(b);
                
            }
        }
        
        foreach (string c in a){
            if (a.Where(x=>x == c).Count() == 2){
                answer += 1;
                // a.Remove(c);
                // a.Remove(c);
            }
        }
        
        
        return answer/2;
    }
}