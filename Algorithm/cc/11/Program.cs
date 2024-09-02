using System;
using System.Collections.Generic;


public class Solution {
    public int[] solution(int[] numbers) {
        int[] answer = new int[] {};
        
        for (int i = 0; i < numbers.Length; i ++)
            numbers[i] = numbers[i] * 2;
        
        return numbers;
    }
}