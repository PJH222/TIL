using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int solution(int[] numbers) {
        int answer = 0;
        List<int> a = numbers.ToList();
        int b = numbers.Length;
        a.Sort();
        if (a[0] * a[1] > a[b - 1] * a[b - 2]){
            return a[0] * a[1];
        }
        else {
            return a[b  - 1] * a[b - 2];
        }
        
        return answer;
    }
}