//Write your code here
finally {
int min=A[0],max=A[0];
for(int j=0;j<A.length;j++)
    {
    if(A[j]>max)
        max=A[j];
    if(A[j]<min)
        min=A[j];
}
System.out.println(max + " " + min);
}

}
