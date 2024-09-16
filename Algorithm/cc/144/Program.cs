using System;
using System.Linq;
using System.Collections.Generic;
public class Solution {
    public bool solution(bool x1, bool x2, bool x3, bool x4) {
        bool answer = false;
        List<bool> tmp = new List<bool>{x1,x2};
        List<bool> tmp2 = new List<bool>{x3,x4};
        
        if ((tmp.Where(x=>(x == true)).Count() >= 1)&&(tmp2.Where(x=>(x == true)).Count() >= 1)) return true;
        
        
        
        return answer;
    }
}