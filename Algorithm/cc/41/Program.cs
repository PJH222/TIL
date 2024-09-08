using System;

public class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        string aa = "";
        int bb = 1;
        int dd = 0;
        aa += a.ToString() + b.ToString();
        
        int cc = int.Parse(aa);
        bb = 2 * a * b;
        
        if (cc > bb){
            return cc;
        }
            
            
        
        return bb;
    }
}