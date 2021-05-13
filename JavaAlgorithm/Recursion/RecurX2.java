package Recursion;

import java.util.Arrays;
import java.util.EmptyStackException;
import java.util.Scanner;

public class RecurX2 {

    public static class IntStack{

        int[] stack;
        int size;
        int max;

        IntStack(int capacity) {
            this.max = capacity;
            this.stack = new int[capacity];
            this.size = 0;
        }

        void push(int n){
            if (size < max) {
                stack[size++] = n;
            } else throw new StackOverflowError("가득참");
        }

        int pop() {
            if (size == 0) {
                throw new EmptyStackException();
            }
            return stack[--size];
        }

        boolean isEmpty() {
            return size == 0;
        }
    }

    static void recur(int n) {
        IntStack s = new IntStack(n);

        while (true) {
            if (n > 0) {
                s.push(n);
                n -= 1;
                continue;
            }

            if (!s.isEmpty()) {
                n = s.pop();
                System.out.println(n);
                n -= 2;
                continue;
            }
            break;
        }
    }

    public static void main(String[] args) {

        Scanner stdIn = new Scanner(System.in);
        int x = stdIn.nextInt();
        recur(x);

    }
}
