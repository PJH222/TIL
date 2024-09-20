using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int solution(int a, int b, int c, int d) {
        int answer = 0;
        List<int> nums = new List<int>{a,b,c,d};
        List<int> eql = new List<int>();
        
        for (int i = 0 ; i < 4 ; i++){
            int z = nums.Where(x => x == nums[i]).Count();
            eql.Add(z);
        }
        
        if (eql.Where(x => x == 4).Count() == 4) {
            return a * 1111;
        }
        else if (eql.Where(x => x == 3).Count() == 3) {
            int e = (nums[eql.IndexOf(3)] * 10 + nums[eql.IndexOf(1)]);
            return e * e;
        }
        else if (eql.Where(x => x == 2).Count() == 4) {
            int maxx = nums.Max();
            int minn = nums.Min();
            return (maxx + minn) * Math.Abs(maxx - minn);
        }
        else if (eql.Where(x => x == 1).Count() == 4) {
            return nums.Min();
        }
        else if (eql.Where(x => x == 2).Count() == 2) {
            int start = eql.IndexOf(2);
            int end = eql.LastIndexOf(2);
            int zzz = 1;
            for (int k = 0 ; k < 4 ; k++){
                if ((k != start) && (k != end)) {
                    zzz *= nums[k];
                }
            }
            return zzz;
            
        }
        
        
        return answer;
    }
}