using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int solution(int i, int j, int k) {
        int answer = 0;
        List<int> aa = new List<int>();
        
        for (int x = i; x<=j ; x ++){
            aa.Add(x);
        }
        string bb = String.Join("",aa);
        answer = bb.Where(x => (x.ToString() == k.ToString())).Count();
        // Console.Write(bb);
        
        return answer;
    }
}