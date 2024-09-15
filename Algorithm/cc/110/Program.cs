using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int solution(int a, int b, int c) {
        int answer = 0;
        List<int> aa = new List<int> {a,b,c};
        List<int> bb = new List<int> {aa.Where(x => x.Equals(a)).Count(),aa.Where(x => x.Equals(b)).Count(),aa.Where(x => x.Equals(c)).Count()};
        
        if ((bb.Where(x => x.Equals(1))).Count() == 3) {
            return a+b+c;
        }
        else if ((bb.Where(x => x.Equals(2))).Count() == 2) {
            return (a+b+c)*(a*a +b*b + c*c);
        }
        else if ((bb.Where(x => x.Equals(3))).Count() == 3) {
            return (a+b+c)*(a*a +b*b + c*c) * (a*a*a + b*b*b + c*c*c);
        }
        
        return answer;
    }
}