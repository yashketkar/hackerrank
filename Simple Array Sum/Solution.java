import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        int n,sum=0;
        Scanner sc= new Scanner (System.in);
        n=sc.nextInt();
        for(int i=0;i<n;i++)
            {
        sum+=sc.nextInt();
        }
        System.out.println(sum);
    }
}
