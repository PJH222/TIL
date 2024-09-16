using System;
using System.Linq;

public class Solution {
    public int solution(int[] array) {
        int answer = 0;
        foreach (int a in array){
            answer += a.ToString().Where(x => (x == '7')).Count();
        }
        return answer;
    }
}