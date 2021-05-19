package string;

import java.util.Scanner;

public class IndexTester {

    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);
        String txt = stdIn.next();
        String pat = stdIn.next();

        int idx1 = txt.indexOf(pat);
        int idx2 = txt.lastIndexOf(pat);
        System.out.println("idx1 = " + idx1);
        System.out.println("idx2 = " + idx2);
    }
}
