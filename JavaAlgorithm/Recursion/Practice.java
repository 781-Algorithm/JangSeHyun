package Recursion;

import java.util.Scanner;

public class Practice {

    static void recur3(int n) {
        if (n > 0) {
            recur3(n - 1);
            recur3(n - 2);
            System.out.println("n = " + n);
        }
    } // Problem 1 위 함수를 비 재귀적으로 구현하기

    static void answer1(int n) {

        int a = 0;

        RecurX2.IntStack intStack = new RecurX2.IntStack(n);
        RecurX2.IntStack intStack2 = new RecurX2.IntStack(n);

        while (true) {
            if (n > 0) {
                intStack.push(n);
                intStack2.push(a);

                if (a == 0) {
                    n -= 1;
                } else if (a == 1) {
                    n -= 2;
                    a = 0;
                }
                continue;
            }

            do {
                n = intStack.pop();
                a = intStack2.pop() + 1;

                if (a == 2) {
                    System.out.println(n);
                    if (intStack2.isEmpty()) {
                        return;
                    }
                }
            } while (a == 2);

        }


    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        answer1(n);
    }
}

