using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int[] solution(int[] arr) {
        int[] answer = new int[] {};
        int z = arr.Where(x => x==2).Count();
        if (arr.Where(x => x==2).Count() == 0) {
            int[] ccc = {-1};
            return ccc;
        }
        
        if (arr.Where(x => x==2).Count() == 1) {
            int[] ccc = {2};
            return ccc;
        }
        
        for (int i = 0 ; i<arr.Length ; i++){
            if (arr[i] != 2) continue;
            for (int j = i ; j<arr.Length ; j++){
                // var a = new ArraySegment<int>(arr,i,j);
                // var slice = arr[i..(j + 1)];
                // Console.WriteLine(j);
                // Console.WriteLine();

                List<int> a = new List<int> (arr.Skip(i).Take(j-i));
                if (a.Where(x => x==2).Count() == z ) {
                    answer = a.ToArray();
                    return answer;
                }
                // foreach (int b in a){
                //     Console.WriteLine(b);
                // }
                // Console.WriteLine();
                
            }
        }
        
        return answer;
    }
}