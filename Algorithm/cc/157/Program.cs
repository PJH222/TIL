using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public string[] solution(string my_str, int n) {
        List<string> answer = new List<string>();
        for (int i = 0; i<my_str.Length ; i += n){
            if (i + n - 1 <= my_str.Length) {
                string a = my_str.Substring(i,n);
                answer.Add(a);
            }
            else {
                string b = my_str.Substring(i, my_str.Length - i);
                answer.Add(b);

            }
        }
        
        return answer.ToArray();
    }
}