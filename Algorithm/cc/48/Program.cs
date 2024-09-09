using System;
using System.Linq;

public class Solution {
    public int[] solution(int[] arr, int k) {
        // int[] answer = new int[] {};
        if (k%2 == 1){
            for (int i = 0; i < arr.Length; i++){
                arr[i] = arr[i] * k;
            }
        }
        else{
            for (int i=0 ; i < arr.Length; i++){
                arr[i] += k;
            }
        }
        int[] answer = arr.ToArray();
        
        return answer;
    }
}