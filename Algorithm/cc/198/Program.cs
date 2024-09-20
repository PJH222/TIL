using System;
using System.Linq;
public class Solution {
    public int solution(int[] array) {
        int answer = 0;
        int maxx = 0;
        int[] a = new int[1000];
        
        for (int i = 0 ; i < array.Length ; i++) {
            int b = array.Where(x => x == array[i]).Count();
            a[array[i]] = b;
            
            if (b >= maxx) {
                maxx = b; 
                answer = array[i];
            }
            
        }
        
        // foreach (int i in a){
        //     // Console.WriteLine(i);
        // }
        foreach (int i in a){
            if (a.Where(x => x==maxx).Count() > 1) return -1;
        }
        
        return answer;
    }
}