package Recursion;

import java.util.Scanner;

public class BOJ11729 {

    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);
        int n = stdIn.nextInt();
        System.out.println((int) Math.pow(2,n)-1);
        hanoi(n,1,2,3);

    }

    public static void hanoi(int no, int a, int b, int c) {

        if(no>=1){
            hanoi(no-1,a,c,b);
            System.out.printf("%d %d\n",a,c);
            hanoi(no-1,b,a,c);
        }

    }

}
