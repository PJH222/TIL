using System;
using System.Linq;
using System.Collections.Generic;

public class Solution {
    public int solution(int[] numbers, int k) {
        int answer = 0;
        int a = numbers.Length;
        for (int i = 0; i < 2000 ; i++){
            if (numbers.Length + 1 < 2*k){
                numbers = numbers.Concat(numbers).ToArray();
            }
        }
        Console.Write(numbers.Length);
        return numbers[(k-1)*2];
    }
}