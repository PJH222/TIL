using System;

public class Solution {
    public string solution(string n_str) {
        // string answer = "";
        for (int i = 0 ; i<n_str.Length ; i++){
            char a = n_str[i];
            Console.Write(a);
            if (a == '0'){
                continue;
            }
            else{
                int num = i;
                string answer = n_str.Substring(num , n_str.Length - num );
                return answer;
            }
        }
        
        // string answer = n_str.Substring(num , n_str.Length - num - 1);
        
        return n_str;
    }
}

// 기본적으로 {}로 나뉘어져 있으면 그 안에서만 변수를 사용할 수 있다... 미친거 아님??