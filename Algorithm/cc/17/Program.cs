using System;
using System.Collections.Generic;

public class Solution {
    public int[] solution(int[] numbers, int num1, int num2) {
        int[] answer = new int[] {};
        List<int> aa = new List<int>();
        
        for (int i=num1; i<=num2; i++){
            aa.Add(numbers[i]);
            
        }
        
        Console.WriteLine(String.Join(" ",aa));
        
        return aa.ToArray();
    }
}