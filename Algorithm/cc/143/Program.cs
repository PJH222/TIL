using System;
using System.Linq;
using System.Collections.Generic;
public class Solution {
    public string solution(string s) {
        List<string> answer = new List<string>();
        for (int i = 0 ; i<s.Length ;i ++){
            if (s.Where(x => (x == s[i])).Count() == 1){
                answer.Add(s[i].ToString());
            }
        }
        answer.Sort();
        return String.Join("",answer);
    }
}