using System;

public class Solution {
    public int solution(string t, string p) {
        int answer = 0;
        long a = t.Length;
        long b = p.Length;
        int cnt = 0;
        while (cnt <= a - b){
            string str = "";
            int zz = 0;
            while (zz < b){
                str += t[zz + cnt];
                zz ++;
            }
            
            long aa = long.Parse(str);
            long bb = long.Parse(p);
            
            if (aa <= bb) answer += 1;
            cnt++;
        }
        
        
        return answer;
    }
}