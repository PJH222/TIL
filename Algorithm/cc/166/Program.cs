using System;
using System.Collections.Generic;
using System.Linq;
public class Solution {
    public int[] solution(int[] arr) {
        List<int> stk = new List<int>();
        int i = 0;
        
        while (i != arr.Length){
            if (stk.Count == 0) {
                stk.Add(arr[i]);
                i += 1;    
            }
            
            else if ((stk.Count > 0)&&(stk[stk.Count - 1] < arr[i])){
                stk.Add(arr[i]);
                i += 1;
            }
            
            else if ((stk.Count > 0)&&(stk[stk.Count - 1] >= arr[i])){
                stk.RemoveAt(stk.Count - 1);
            }
            
            if (i == arr.Length) break;
            // foreach (int a in stk){
            //     Console.WriteLine(a);
            // }
        }
        
        return stk.ToArray();
    }
}