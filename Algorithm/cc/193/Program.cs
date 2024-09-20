using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int[] solution(int l, int r) {
        List<int> answer = new List<int>();
        for (int i = 0; i <= r ; i += 5){
            if (i < l){
                continue;
            }
            
            int a = (i.ToString()).Length;
            int b = (i.ToString()).Where(x => (x == '5')).Count();
            int c = (i.ToString()).Where(x => (x == '0')).Count();
            
            if (a == (b+c)) {
                answer.Add(i);
            }
        }
        if (answer.Count == 0){
            answer.Add(-1);
        }
        return answer.ToArray();
    }
}