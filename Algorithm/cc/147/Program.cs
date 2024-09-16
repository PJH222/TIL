using System;
using System.Collections.Generic;
using System.Linq;
public class Solution {
    public int solution(string[] strArr) {
        int answer = 0;
        List<int> a = new List<int>(); // 문자열 길이만 저장
        List<int> b = new List<int>(); // 문자열 길이와 동일한 문자열 목록 개수
        int indict = 0; // 최적화용
        for (int i = 1; i <= 30; i++){
            int tmp = 0;
            for (int j = 0; j < strArr.Length ; j ++){
                if (strArr[j].Length == i) {
                    tmp += 1;
                    indict += 1;
                }
            }
            b.Add(tmp);
            if (indict == strArr.Length) break; // 최적화용
        }
        
        return b.Max();
    }
}