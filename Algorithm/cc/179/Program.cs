using System;

public class Solution {
    public int solution(string[] spell, string[] dic) {
        int answer = 2;
        for (int i = 0; i<dic.Length ; i++) {
            
            if (dic[i].Length < spell.Length) continue;
            
            for (int j = 0 ; j < dic[i].Length ; j++) {
                for (int k = 0 ; k < spell.Length ; k++) {
                    if (dic[i].IndexOf(spell[k]) == -1) {
                        break;
                    }
                    
                    if (k == spell.Length - 1) return 1;
                }
                }
            }
        
        return answer;
    }
}