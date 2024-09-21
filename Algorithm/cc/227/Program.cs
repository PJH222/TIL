using System;
using System.Linq;
using System.Collections.Generic;

public class Solution {
    public int[] solution(int[] arr) {
        int[] answer = new int[] {};
        int minn = arr.Min();        
        int[] minus = new int[]{-1};
        
        
        answer = arr.Where(x => x!=minn).ToArray();
        if (answer.Length == 0){
            answer = minus;
        }
        return answer;
    }
}