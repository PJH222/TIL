using System;
using System.Linq;

public class Solution {
    public int[,] solution(int n) {
        int[,] answer = new int[n,n];
        
        string mode = "right";
        int i = 0;
        int j = 0;
        int cnt = 1;
        if (n==1) {
            answer[0,0]=1;
            return answer;
        }
        else if (n==2) {
            answer[0,0]=1;
            answer[0,1]=2;
            answer[1,1]=3;
            answer[1,0]=4;
            return answer;
        }
        
        
        
        while (true){
            if (mode == "right"){
                if (answer[i,j+1] != 0){
                    mode = "down";
                    continue;
                }
                answer[i,j] = cnt;
                cnt += 1;
                j += 1;
                
                if ((j + 1 == n) || (answer[i,j+1] != 0)){
                    mode = "down";
                    answer[i,j] = cnt;
                    cnt += 1;
                    i += 1;
                }
            }
            else if (mode == "down"){
                if (answer[i+1,j] != 0){
                    mode = "left";
                    continue;
                }
                answer[i,j] = cnt;
                cnt += 1;
                i += 1;
                
                if ((i + 1 == n) || (answer[i + 1,j] != 0)){
                    mode = "left";
                    answer[i,j] = cnt;
                    cnt += 1;
                    j -= 1;
                }
            }
            else if (mode == "left"){
                if (answer[i,j-1] != 0){
                    mode = "up";
                    continue;
                }
                answer[i,j] = cnt;
                cnt += 1;
                j -= 1;
                
                if ((j - 1 < 0) || (answer[i,j - 1] != 0)){
                    mode = "up";
                    answer[i,j] = cnt;
                    cnt += 1;
                    i -= 1;
                }
            }
            else if (mode == "up"){
                if (answer[i-1,j] != 0){
                    mode = "right";
                    continue;
                }
                answer[i,j] = cnt;
                cnt += 1;
                i -= 1;
                
                if ((i - 1 < 0) || (answer[i - 1,j] != 0)){
                    mode = "right";
                    answer[i,j] = cnt;
                    cnt += 1;
                    j += 1;
                }
            }
            // Console.WriteLine("i:{0},  j:{1}",i,j);
            // Console.WriteLine("현재모드 : {0},  cnt : {1}",mode,cnt);
            if (cnt >= n * n) break;
                
            
        }
        
        
        return answer;
    }
}