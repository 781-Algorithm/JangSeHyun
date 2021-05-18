package recursion;

import java.util.Scanner;

public class Factorial {

    static int factorial(int n){
        if (n>0){
            return n * factorial(n - 1);
        }
        else{
            return 1;
        }
    }

    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);
        int x = stdIn.nextInt();

        System.out.println("factoral(x) is Equal to " + factorial(x));
    }
}
