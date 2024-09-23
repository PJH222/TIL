using System;

public class Solution {
    public string solution(int[] food) {
        string answer = "0";
        string start = "";
        for (int i = 1; i<food.Length ;i++){
            if (food[i]%2 == 1){
                for (int j=0; j<(food[i]-1)/2 ;j++){
                    start += (i).ToString();
                }
            }
            else {
                for (int j=0; j<(food[i])/2 ;j++){
                    start += (i).ToString();
                }
            }
        }
        start += "0";
        
        for(int i=start.Length - 2; i>=0; i--){
            start += start[i];
        }
        
        
        return start;
    }
}