using System;
using System.Linq;
public class Solution {
    public int solution(string A, string B) {
        int answer = 0;
        string aa = "";
        int a = 0; // 왼쪽으로 밀 경우
        int b = 0; // 왼쪽으로 밀 경우
        if (A == B) return 0;
        
        
        for (int i = 0 ; i < A.Length ; i++){
            if (i == 0){
                aa = A.Insert(0,(A[A.Length - 1]).ToString());
                
            }
            else {
                aa = aa.Insert(0,(aa[aa.Length - 1]).ToString());
                
            }
            
            if (aa.IndexOf(B) != -1) {
                a = i + 1;
                break;
            }
            aa = aa.Remove(aa.Length - 1 , 1);
            Console.WriteLine(aa);
        }
        if (a == 0) return -1;
        
        return a;
    }
}