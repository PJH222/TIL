using System.Collections.Generic;

public class Solution {
    public long[] solution(int x, int n) {
        List<long> answer = new List<long>();
        long a = x;
        if (a == 0) {
            for (int i = 0 ; i < n ; i++){
                answer.Add(0);
            }
            return answer.ToArray();
        }
            
        
        if (x >= 0){
            for (long i = x; i <= a * n; i += a){
                answer.Add(i);
            }
        }
        else {
            for (long i = x; i >= a * n; i += a){
                answer.Add(i);
            }
        }
        
        return answer.ToArray();
    }
}