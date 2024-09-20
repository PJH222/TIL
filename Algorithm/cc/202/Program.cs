using System;

public class Solution {
    public int solution(int[,] board) {
        int answer = 0;
        
        for (int i = 0 ; i<board.GetLength(0) ; i++){
            for (int j = 0 ; j<board.GetLength(1) ; j++){
                if (board[i,j] == 1){
                    // 우하단
                    if ((j + 1 < board.GetLength(1)) && (i + 1 < board.GetLength(0)) && (board[i+1,j+1] == 0)){
                        board[i+1,j+1] = 2;
                        answer += 1;
                        Console.WriteLine("경우 5");
                    }
                    // 우상단
                    if ((j + 1 < board.GetLength(1)) && (i - 1 >= 0) && (board[i-1,j+1] == 0)){
                        board[i-1,j+1] = 2;
                        answer += 1;
                        Console.WriteLine("경우 6");
                    }
                    // 좌상단
                    if ((j - 1 >= 0) && (i - 1 >= 0) && (board[i-1,j-1] == 0)){
                        board[i-1,j-1] = 2;
                        answer += 1;
                        Console.WriteLine("경우 7");
                    }
                    // 좌하단
                    if ((j - 1 >= 0) && (i + 1 < board.GetLength(0)) && (board[i+1,j-1] == 0)){
                        board[i+1,j-1] = 2;
                        answer += 1;
                        Console.WriteLine("경우 8");
                    }
                    // 하단
                    if ((i + 1 < board.GetLength(0)) && (board[i+1,j] == 0))  {
                        board[i + 1,j] = 2;
                        answer += 1;
                        Console.WriteLine("경우 1");
                        }
                    // 상단
                    if ((i - 1 >= 0) && (board[i-1,j] == 0)) {
                        board[i - 1,j] = 2;
                        answer += 1;
                        Console.WriteLine("경우 2");
                        }
                    // 우단
                    if ((j + 1 < board.GetLength(1)) && (board[i,j+1] == 0)) {
                        board[i,j + 1] = 2;
                        answer += 1;
                        Console.WriteLine("경우 3");
                        }
                    // 좌단
                    if ((j - 1 >= 0)&& (board[i,j-1] == 0))  {
                        board[i,j - 1] = 2;
                        answer += 1;
                        Console.WriteLine("경우 4");
                        }
                    
                    
                    board[i,j] = 2;
                    answer += 1;
                    
                    
                }
            }
        }
        int nn = board.GetLength(0);
        for (int i = 0 ; i<nn ; i++){
            for (int j = 0 ; j<nn ; j++){
                Console.Write(board[i,j]);
            }
            Console.WriteLine();
        }
        
        return board.GetLength(0) * board.GetLength(1) - answer;
    }
}