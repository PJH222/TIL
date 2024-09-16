using System;
using System.Linq;
using System.Collections.Generic;

public class Solution {
    public int[] solution(int[] arr) {
        int[] answer = new int[] {};
        int a = arr.Where(x=>x==2).Count();
        
        if (a == 0){
            int[] b = new int[]{-1};
            return b;
        }
        int start = Array.IndexOf(arr, 2);
        int end = Array.LastIndexOf(arr, 2);
        
        answer = arr.Skip(start).Take(end - start + 1).ToArray();

        
        foreach (int bb in answer) Console.WriteLine(bb);
        return answer;
    }
}