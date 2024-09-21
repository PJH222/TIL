public class Solution {
    public string solution(double num) {
        string answer = num.ToString();
        int a = int.Parse(answer[answer.Length - 1].ToString());
        if (a % 2 == 1) return "Odd";
        return "Even";
    }
}