using System;
using System.Linq;
using System.Collections.Generic;

public class Solution {
    public int[] solution(int[] array) {
        int[] answer = new int[] {0,0};
        int a = 0;
        int b = 0;
        
        
        for (int i = 0 ; i < array.Length; i++){
            if (array[i] > b){
                b = array[i];
                a = i;
            }
        }
//         Console.WriteLine(a);
//         Console.WriteLine(b);
        
        answer[0] = b;
        answer[1] = a;
        
        return answer;
    }
}