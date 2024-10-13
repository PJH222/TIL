using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int solution(string s) {
        int answer = 0;        
        List<char> a = s.ToList();
        
        char start = '1'; // x 대용
        int equ = 0;
        int diff = 0;
        
        
        for (int i=0 ; i<a.Count ; i++){
            if (start == '1') {
                start = a[i];
                equ++;
            }
            else {
                if (a[i] == start){
                    equ++;
                    if (equ == diff){
                        answer++;
                        start = '1';
                        equ = 0;
                        diff = 0;
                    }
                } else {
                    diff++;
                    if (equ == diff){
                        answer++;
                        start = '1';
                        equ = 0;
                        diff = 0;
                    }
                }
            }
        }
        if ((equ != 0) | (diff != 0)) answer++;
        
        
        return answer;
    }
}