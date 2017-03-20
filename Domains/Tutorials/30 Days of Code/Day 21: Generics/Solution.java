/**
*    Method Name: printArray
*    Print each element of the generic array on a new line. Do not return anything.
*    @param A generic array
**/
public static <T> void printArray( T[] inputArray ) {
    // Display array elements
    for(T element : inputArray){
        System.out.printf("%s\n", element);
    }
}
