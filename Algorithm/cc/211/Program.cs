using System.Collections.Generic;

public class Solution {
    public long[] solution(int x, int n) {
        List<long> answer = new List<long>();
        if (x >= 0){
            for (int i = x; i <= x * n; i += x){
                answer.Add(i);
            }
        }
        else {
            for (int i = x; i >= x * n; i += x){
                answer.Add(i);
            }
        }
        
        return answer.ToArray();
    }
}