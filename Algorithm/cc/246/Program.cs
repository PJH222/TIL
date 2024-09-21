using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int[] solution(string s) {
        List<int> answer = new List<int>();
        for (int i = 0 ; i<s.Length ;i++){
            if (s.IndexOf(s[i]) == i){
                answer.Add(-1);
            }
            // else if (s.IndexOf(s[i]) != i){
            //     answer.Add(i-s.IndexOf(s[i]));
            // }
            else if (s.Where(x => x==s[i]).Count() >= 2){
                string tmp = "";
                for (int j = i; j >= 0; j--){
                    tmp += s[j];
                    if (tmp.Where(x => x== s[i]).Count() == 2){
                        // Console.WriteLine(tmp);
                        answer.Add(i-j);
                        break;
                    }
                }
            }
            
            
        }
        return answer.ToArray();
    }
}