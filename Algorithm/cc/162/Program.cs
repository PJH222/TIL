using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int solution(int[] arr) {
        int answer = 0;
        int cnt = 0;
        int[] arr2 = arr;
        List<string> tmp = new List<string>() {String.Join(" ",arr)};
        
        while (true) {
            for (int i = 0 ; i<arr.Length ; i++){
                if ((arr[i]>=50)&&(arr[i]%2 == 0)) arr[i] /= 2;
                else if ((arr[i]<50)&&(arr[i]%2 == 1)) arr[i] = arr[i] * 2 + 1;
            }
            string b = String.Join(" ",arr);
            // Console.WriteLine(b);
            
            if (tmp.IndexOf(b) == -1) {
                tmp.Add(String.Join(" ",arr));
            }
            
            else return cnt;
            cnt += 1;
            

        }
        
        
        
        return answer;
    }
}