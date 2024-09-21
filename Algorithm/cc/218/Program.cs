using System;
// using System.
public class Solution {
    public long solution(long n) {
        double answer = Math.Pow(n,0.5);
        // List<int> a = new List<int>();
        for (int i = 1 ; i<Math.Pow(50000000000000,0.5) ; i++){
            if (i == answer){
                return (long)Math.Pow(i + 1,2);
            }
            if (i > answer) return (long)-1;
        }
        
        return (long)-1;
    }
}