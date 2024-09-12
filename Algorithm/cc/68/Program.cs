using System;
using System.Linq;
public class Solution {
    public int solution(int[] arr1, int[] arr2) {
        int answer = 0;
        if (arr1.Length > arr2.Length){
            return 1;
        }
        else if (arr1.Length < arr2.Length){
            return -1;
        }
        else {
            if (arr1.Sum() > arr2.Sum()){
                return 1;
            }
            else if (arr1.Sum() < arr2.Sum()){
                return -1;
            }
            else{
                return 0;
            }
        }
        
        
        return answer;
    }
}