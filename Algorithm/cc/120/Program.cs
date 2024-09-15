using System;
using System.Collections.Generic;

public class Solution {
    public string solution(string my_string, int m, int c) {
        string answer = "";
        List<string> aa = new List<string>();
        for (int i = 0 ; i<my_string.Length ; i += m){
            string b = "";
            for (int j = i; j<m + i ; j ++){
                b += my_string[j];
            }
            aa.Add(b);
        }
        foreach (string cc in aa){
            Console.WriteLine(cc);
            answer += cc[c - 1];
        }
        
        return answer;
    }
}