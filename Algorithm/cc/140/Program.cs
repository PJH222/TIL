using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int solution(string my_string) {
        int answer = 0;
        string a = "abcdefghijklmnopqrstuvwxyz";
        string aa = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        string tmp = "";
        foreach (char c in my_string){
            if (char.IsDigit(c) == false){
                tmp += " ";
            }
            else {
                tmp += c;
            }
        }
        Console.Write(tmp);
        // tmp = tmp.Replace(" ","");
        List<string> tmp2 = tmp.Split().ToList();
        
        foreach (string aaa in tmp2){
            if (aaa != "") {
                answer += int.Parse(aaa);
            }
        }
        
        return answer;
    }
}