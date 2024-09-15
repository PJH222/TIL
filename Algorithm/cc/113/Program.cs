using System;

public class Solution {
    public int solution(int[,] arr) {
        int answer = 1;
        // Console.Write((arr.GetRow(0)).Length);
        for (int i = 0; i<arr.GetLength(0) ; i++){
            for (int j = 0 ; j < arr.GetLength(0); j++){
                if (arr[i,j] != arr[j,i]){
                    return 0;
                }
            }
        }
        return answer;
    }
}