using System;
using System.Collections.Generic;
using System.Linq;


public class Solution {
    public int solution(string[] babbling) {
        int answer = 0;
        List<string> str = new List<string>{"aya", "ye", "woo", "ma"};
        List<string> str_lis = new List<string>{"ayaaya", "yeye", "woowoo", "mama"};
        int indict = 0;
        foreach (string a in babbling){
            foreach (string b in str_lis){
                if (a.IndexOf(b) != -1){
                    indict = 1;
                    break;
                }
            }
            if (indict == 1) {
                indict = 0;
                continue;
            }
            string c = a;
            int tmp1 = 0;
            int tmp2 = 0;
            
            for (int i=0 ;i<15 ;i++){
                for (int j=0 ;j<4 ;j++){
                    if (c.IndexOf(str[j]) == 0){
                        tmp1 = str[j].Length;
                        tmp2 = c.Length - tmp1;
                        c = c.Substring(tmp1, tmp2);
                    }
                }
            }
            if (c.Length == 0) answer++ ;
                
            
            
        }
        
       
        
        
        
        return answer;
    }
}