package Recursion;

import java.util.Scanner;

public class EuclidGcd {

    static int gcd(int x, int y){
        if (y == 0) {
            return x;
        } else {
            return gcd(y, x % y);
        }
    }

    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);
        int a = stdIn.nextInt();
        int b = stdIn.nextInt();
        System.out.println("GCD of two num is " + gcd(a, b));
    }
}
