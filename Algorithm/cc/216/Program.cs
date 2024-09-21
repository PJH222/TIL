public class Solution {
    public int[] solution(long n) {
        string a = n.ToString();
        
        int[] answer = new int[a.Length];
        
        for (int i = 0; i<a.Length ; i++){
            answer[i] = a[a.Length - i - 1] - 48;
        }
        
        return answer;
    }
}