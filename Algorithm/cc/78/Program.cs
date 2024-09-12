using System;
using System.Collections.Generic;

public class Solution {
    public int[] solution(string myString) {
        List<int> answer = new List<int>();
        // for (int i = 0; i < (myString.Split("x")).Length; i++){
        //     Console.Write(myString.Split("x"));
        // }
        foreach (var value in myString.Split("x"))
        {
            answer.Add(value.Length);
        }
        
        return answer.ToArray();
    }
}