using System;

public class Solution {
    public int[] solution(string[] keyinput, int[] board) {
        int[] answer = new int[2]{0,0};
        int max_x = (board[0] - 1) / 2;
        int min_x = (board[0] - 1) / 2 * -1;
        
        int max_y = (board[1] - 1) / 2;
        int min_y = (board[1] - 1) / 2 * -1;
        
        Console.WriteLine(max_x);
        Console.WriteLine(min_x);
        Console.WriteLine(max_y);
        Console.WriteLine(min_y);
        
        
        foreach (string str in keyinput){
            if (str == "left") {
                if (answer[0] > min_x) {
                    answer[0] -= 1;
                }
            }
            else if (str == "right") {
                if (answer[0] < max_x) {
                    answer[0] += 1;
                }
            }
            else if (str == "up") {
                if (answer[1] < max_y) {
                    answer[1] += 1;
                }
            }
            else if (str == "down") {
                if (answer[1] > min_y) {
                    answer[1] -= 1;
                }
            }
        }
        
        return answer;
    }
}