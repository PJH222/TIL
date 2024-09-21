using System;

public class Solution {
    public bool solution(int x) {
        bool answer = false;
        string c = x.ToString();
        int a = 0;
        
        for (int i = 0; i < c.Length ; i++){
            a += int.Parse(c[i].ToString());
        }        
        
        if (x%a == 0) return true;
        
        return answer;
    }
}