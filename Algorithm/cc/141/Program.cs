using System;
using System.Linq; 
public class Solution {
    public int solution(string before, string after) {
        int answer = 1;
        for (int i = 0 ; i<before.Length ; i++){
            int a = before.Where(x => (x == before[i])).Count();
            int b = after.Where(x => (x == before[i])).Count();
            if (a!=b) return 0;
        }
        return answer;
    }
}