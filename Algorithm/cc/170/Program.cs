using System;
using System.Text;

public class Solution {
    public string solution(string a, string b) {
        string answer = "";
        StringBuilder str = new StringBuilder();
        
        int maxx = Math.Max(a.Length, b.Length);
        
        int tmp = 0;
        
        for (int i = 0 ; i<maxx ; i++){
            int a_i = i < a.Length ? a[a.Length - 1 - i] - '0' : 0;
            int b_i = i < b.Length ? b[b.Length - 1 - i] - '0' : 0;
            
            int sum_ab = a_i + b_i + tmp;
            tmp = sum_ab / 10; // 십자리 수로 올라 가는 값
            
            str.Insert(0, sum_ab % 10);
            
        }
        if (tmp > 0) str.Insert(0, tmp);
        
        return str.ToString();
    }
}