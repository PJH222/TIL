using System;
using System.Linq;

public class Solution {
    public string[] solution(string[] str_list) {
        string[] answer = new string[] {};
        for (int i = 0 ; i<str_list.Length ; i++){
            if (str_list[i]=="l") {
                answer = str_list.Take(i).ToArray();
                return answer;
            }
            else if (str_list[i]=="r") {
                answer = str_list.Skip(i + 1).Take(str_list.Length - i + 1).ToArray();
                return answer;
            }
        }
        return answer;
    }
}