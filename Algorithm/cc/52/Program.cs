using System;

public class Solution {
    public int solution(int[] num_list, int n) {
        int answer = 0;
        string aa = "";
        
        aa = String.Join(" ",num_list);
        Console.WriteLine(aa);
        
        if (aa.IndexOf(n.ToString()) != -1){
            return 1;
        }
        
        
        return 0;
    }
}