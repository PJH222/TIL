using System;

public class Solution {
    public int[] solution(string[] keymap, string[] targets) {
        int[] answer = new int[targets.Length];
        
        for(int i=0 ;i<targets.Length ;i++){    
            for(int j=0; j<targets[i].Length ; j++){
                int minn = 102;
                int indict = 0; // 키에 없는 알파뱃이 등장한 경우 -1로 빼기 위한 변수.
                
                Console.WriteLine(targets[i][j]);
                foreach (string str in keymap){
                    if ((minn > str.IndexOf(targets[i][j])) && (str.IndexOf(targets[i][j]) != -1)) {
                        minn = str.IndexOf(targets[i][j]);
                    }
                    else if (str.IndexOf(targets[i][j]) == -1){
                        indict++;
                    }
                }
                
                if (indict == keymap.Length) {
                    answer[i] = -1;
                    break;
                }
                else {
                    answer[i] += minn + 1;
                    Console.WriteLine(minn + 1);
                }
                Console.WriteLine();
            }
        }

        return answer;
    }
}