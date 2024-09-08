using System;

public class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        string aa = "";
        string bb = "";
        
        aa = a.ToString() + b.ToString();
        bb = b.ToString() + a.ToString();
        
        int cc = 0;
        int dd = 0;
        cc = int.Parse(aa);
        dd = int.Parse(bb);
        
        if (cc > dd){
           return cc;
        }
        
        return dd;
    }
}