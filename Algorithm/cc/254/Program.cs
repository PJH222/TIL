using System;
using System.Linq;
using System.Collections.Generic;

public class Solution {
    public string solution(string[] cards1, string[] cards2, string[] goal) {
        string answer = "Yes";
        List<string> tmp = new List<string>();
        for (int i =0; i<goal.Length ;i++){
            if ((cards1.Length > 0) && (cards1[0] == goal[i])){
                tmp = cards1.ToList();
                tmp.RemoveAt(0);
                cards1 = tmp.ToArray();
            }
            else if ((cards2.Length > 0) && (cards2[0] == goal[i])){
                tmp = cards2.ToList();
                tmp.RemoveAt(0);
                cards2 = tmp.ToArray();
            }
            else return "No";
        }
        
        
        return answer;
    }
}