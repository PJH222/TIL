using System.Linq;

public class Solution {
    public double solution(int[] arr) {
        double a = arr.Sum();
        double b = arr.Length;
        return a/b;
    }
}