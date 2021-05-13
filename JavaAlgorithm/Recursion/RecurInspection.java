package Recursion;

import java.util.Scanner;

public class RecurInspection {

    static void recur(int n) {
        if (n > 0) {
            recur(n - 1);
            System.out.println("n = " + n);
            recur(n - 2);
        }
    }

    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);
        int x = stdIn.nextInt();

        recur(x);
    }
    // topdown, bottom-up
}
