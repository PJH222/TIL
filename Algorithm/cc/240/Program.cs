using System;

public class Solution {
    public double solution(int n) {
        int answer = 0;
        string a3 = "";
        int start = 0;
        
        
        for (int i = 3; i < 100000000000001 ; i *= 3){
            if (n / i == 0){
                start = i / 3;
                break;
            }
        }
        
        for (int i = start; i >= 1; i /= 3){
            if (n/i >= 1){
                int a = n/i;
                a3 += a.ToString();
                n = n%i;
                
            }
            else {
                a3 += "0";
            }
        }
        Console.WriteLine(a3);
        string tmp = "";
        for (int i = a3.Length - 1 ; i>=0 ; i--){
            tmp += a3[i];
        }
        
        int zz = 1;
        
        for (int i = tmp.Length - 1 ; i >= 0 ; i --){
            answer += int.Parse(tmp[i].ToString()) * zz;
            zz *= 3;
        }
        
        
        return answer;
    }
}