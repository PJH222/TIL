using System;
using System.Collections.Generic;
using System.Linq;
public class Solution {
    public int[] solution(int[] arr) {
        List<int> answer = arr.ToList();
        int a = arr.Length;
        double b = 0;
        for (int i = 1 ; i<a*a ; i++){
            if (Math.Pow(2,i) >= a) {
                b = Math.Pow(2,i);
                break;
            }
        }
        // Console.Write(b-a);
        for (int i = 0 ; i<b-a ; i++){
            answer.Add(0);
        }
        
        return answer.ToArray();
    }
}