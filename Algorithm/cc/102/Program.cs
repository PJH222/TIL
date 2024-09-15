using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int[] solution(int[] numbers, string direction) {
        List<int> answer = numbers.ToList();
        int a = 0 ;
        
        if (direction == "right"){
            answer = (answer.Prepend(numbers[numbers.Length - 1])).ToList();
            answer.RemoveAt(numbers.Length);
        }
        else {
            answer = (answer.Append(numbers[0])).ToList();
            answer.RemoveAt(0);
        }
        
        return answer.ToArray();
    }
}