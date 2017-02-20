import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc= new Scanner(System.in);
        int n=sc.nextInt();
        double p=0,z=0,m=0;
        int a[] = new int[n];
        for(int j=0;j<n;j++)
        {
            a[j]=sc.nextInt();
            if(a[j]>0)
                {
                p++;
            }
            else if (a[j]<0)
                {
                m++;
            }
            else if (a[j]==0)
                {
                z++;
            }
        }
        System.out.println(p/n);
        System.out.println(m/n);
        System.out.println(z/n);
    }
}
