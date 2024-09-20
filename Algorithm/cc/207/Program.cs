using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int solution(string[] babbling) {
        int answer = 0;
        string[] a = {"aya", "ye", "woo", "ma"};
        List<string> result = new List<string>();
        
        foreach (string b in a){
            foreach (string c in a){
                foreach (string d in a){
                    foreach (string e in a){
                        string f = b+c+d+e;             
                        string g = b+c+d;
                        string h = b+c;
                        string i = b;
                        
                        result.Add(f);
                        result.Add(g);
                        result.Add(h);
                        result.Add(i);
                    }
                }
            }
        }
        
        foreach (string z in babbling){
            if (result.IndexOf(z) != -1) answer += 1;
        }
        
        
        return answer;
    }
}