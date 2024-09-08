using System;

public class Solution {
    public string solution(string my_string, int[] index_list) {
        string answer = "";
        for (int i=0; i < index_list.Length; i++){
            answer += my_string.Substring(index_list[i],1);
        }
        return answer;
    }
}