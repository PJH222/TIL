using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int[] solution(int[] arr, int[] delete_list) {
        List<int> aa = new List<int>();
        
        for (int i=0 ; i < delete_list.Length; i++){
            arr = arr.Where(num => num != delete_list[i]).ToArray();
        }
        
        return arr;
    }
}