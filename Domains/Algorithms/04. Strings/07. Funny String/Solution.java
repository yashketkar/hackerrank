import java.io.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        int n=0;
        Scanner sc=new Scanner(System.in);
        n=sc.nextInt();
        String[] array = new String[n];
        for(int i=0;i<n;i++)
        {
          array[i]=sc.next();
        }
        for(int i=0;i<n;i++)
        {
          System.out.println(funnyOrNot(array[i]));
        }
    }
    public static String funnyOrNot(String input)
        {
          String reverse = new StringBuilder(input).reverse().toString();
          //System.out.println(reverse);
          boolean funny=true;
          int num1=0,num2=0;
          for(int i=1;i<input.length();i++)
          {
            num1 = input.charAt(i)-input.charAt(i-1);
            num2 = reverse.charAt(i)-reverse.charAt(i-1);
            //System.out.println(input.charAt(i) + "\t" + input.charAt(i-1) + "\t" + reverse.charAt(i) + "\t" + reverse.charAt(i-1) + "\t" + reverse.charAt(i-1) + "\t" + num1 + "\t" + num2);
            if(Math.abs(num1)!=Math.abs(num2))
            {
              funny=false;
              break;
            }
          }
          if(funny)
          return "Funny";
          else
          return "Not Funny";
    }
}
