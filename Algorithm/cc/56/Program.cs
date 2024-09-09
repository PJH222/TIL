using System;
using System.Linq;

public class Solution {
    public int[] solution(int[] arr, int n) {
        // int[] answer = new int[] {};
        for (int i = 0 ; i<arr.Length; i++){
            if (arr.Length % 2 == 1){
                if (i%2 == 0){
                    arr[i] += n;
                }
            }
            else{
                if (i%2 == 1){
                    arr[i] += n;
                }
            }
        }
        
        int[] answer = arr.ToArray();
        
        return answer;
    }
}