using System;

public class Example
{
    public static void Main()
    {
        String[] s;

        Console.Clear();
        s = Console.ReadLine().Split(' ');
        
        int a = int.Parse(s[0]);
        
        if (a % 2 == 0){
            Console.WriteLine("{0} is even",a);    
        }
        else{
            Console.WriteLine("{0} is odd",a);   
        }
        // Console.WriteLine(a);
    }
}