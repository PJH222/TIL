using System;
using System.Collections.Generic;

public class Solution {
    public int[] solution(int n) {
        int[] answer = new int[] {};
        List<int> aa = new List<int>();
        
        for (int i=1; i<=n; i += 2){
            aa.Add(i);
        }
        
        Console.WriteLine(String.Join(" ",aa));
        answer = aa.ToArray();
        return answer;
    }
}