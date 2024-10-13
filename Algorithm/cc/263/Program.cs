using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public string solution(string s, string skip, int index) {
        string answer = "";
        string str = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz";
        
        foreach (char cha in s){
            int a = str.IndexOf(cha);
            string b = str.Substring(a, index + skip.Length + 20);
            int cnt = 0;
            
            // Console.WriteLine(str.IndexOf(cha));
            for (int i=0 ;i<b.Length ;i++){
                if ((cnt == index)&&(skip.IndexOf(b[i]) == -1)){
                    answer += b[i];
                    break;
                }
                if (skip.IndexOf(b[i]) == -1) {
                    cnt++;
                }
            }
            
        }
        
            
            
        return answer;
    }
}