import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String S = in.next();
        int count=0;
        char sc[] = S.toCharArray();
        for (int i=0;i<sc.length;i++)
        {
          if(i%3==0)
          {
            if(sc[i]!='S')
            {
              count++;
            }
          }
          if(i%3==1)
          {
            if(sc[i]!='O')
            {
              count++;
            }
          }
          if(i%3==2)
          {
            if(sc[i]!='S')
            {
              count++;
            }
          }
        }
        System.out.print(count);
    }
}
