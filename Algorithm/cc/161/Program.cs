using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int solution(int[] arr) {
        int answer = 0;
        int cnt = 0;
        int[] arr2 = new int[]{};
        List<string> tmp = new List<string>();
        
        while (true) {
            cnt += 1;
            
            for (int i = 0 ; i<arr.Length ; i++){
                if ((arr[i]>=50)&&(arr[i]%2 == 0)) arr[i] /= 2;
                else if ((arr[i]<50)&&(arr[i]%2 == 1)) arr[i] = arr[i] * 2 + 1;
            }
            string b = String.Join("",arr);
            if (tmp.IndexOf(b) == -1) {
                tmp.Add(String.Join("",arr));
            }
            else return cnt - 1;
            

        }
        
        
        
        return answer;
    }
}