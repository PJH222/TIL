using System;
using System.Linq;
using System.Collections.Generic;


public class Solution {
    public double solution(int[] numbers) {
        double answer = 0;
        List<int> intList = new List<int>(numbers);
        int b = intList.Count();
        double sum = intList.Sum();

        

        return sum / b;
    }
}

// 진짜 C# 개토나오네 ;