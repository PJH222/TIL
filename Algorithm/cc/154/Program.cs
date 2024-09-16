using System;
using System.Linq;
using System.Collections.Generic;

public class Solution {
    public int[] solution(int n, int[] slicer, int[] num_list) {
        int[] answer = new int[] {};
        if (n==1) {
            return num_list.Take(slicer[1] + 1).ToArray();
        }
        else if(n==2){
            return num_list.Skip(slicer[0]).Take(num_list.Length - slicer[0]).ToArray();
        }
        else if(n==3){
            return num_list.Skip(slicer[0]).Take(slicer[1] - slicer[0] + 1).ToArray();
        }
        else{
            List<int> aa = new List<int>();
            for (int i = slicer[0] ; i<= slicer[1] ; i += slicer[2]){
                aa.Add(num_list[i]);
            }
            return aa.ToArray();
        }
        
        return answer;
    }
}