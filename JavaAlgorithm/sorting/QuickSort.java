package sorting;

import recursion.RecurX2;

import java.util.Scanner;

public class QuickSort {

    static class Partition {

        static void swap(int[] a, int idx1, int idx2) {
            int t = a[idx1];
            a[idx1] = a[idx2];
            a[idx2] = t;
        }

        static void partition(int[] a, int n) {
            int pl = 0;
            int pr = n - 1;
            int pivot = a[n / 2];

            do {
                while (a[pl] < pivot) pl++;
                while (a[pr] > pivot) pr--;

                if (pl <= pr) {
                    swap(a, pl++, pr--);
                }
            } while (pl <= pr);
        }
    }

    static void quickSort(int[] a, int left, int right) {

        int pl = left;
        int pr = right;
        int pivot = a[(pl + pr) / 2];

        System.out.printf("a[%d]~a[%d] : {", left, right);
        for (int i = left; i < right; i++) {
            System.out.printf("%d ,", a[i]);
        }
        System.out.printf("%d}\n",a[right]); // 절차 showing

        do {
            while (a[pl] < pivot) pl++;
            while (a[pr] > pivot) pr--;

            if (pl <= pr) {
                Partition.swap(a, pl++, pr--);
            }
        } while (pl <= pr);

        if (left < pr) quickSort(a, left, pr);
        if (pl < right) quickSort(a,pl,right);
    }

    static void quickSort_nonRecur(int[] a, int left, int right) {
        RecurX2.IntStack lstack = new RecurX2.IntStack(right - left + 1);
        RecurX2.IntStack rstack = new RecurX2.IntStack(right - left + 1);

        lstack.push(left);
        rstack.push(right);

        while (!lstack.isEmpty()) {
            int pl = left = lstack.pop();
            int pr = right = rstack.pop();
            int x = a[(left + right) / 2]; // 피벗

            do {
                while (a[pl] < x) pl++;
                while (a[pr] > x) pr--;

                if (pl <= pr) {
                    Partition.swap(a, pl, pr);
                }
            } while (pl <= pr);

            if (left < pr) {
                lstack.push(left);
                rstack.push(pr);
            }

            if (right > pl) {
                lstack.push(pl);
                rstack.push(right);
            }
        }
    }

    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);
        int nx = stdIn.nextInt();
        int[] x = new int[nx];
        for (int i = 0; i < nx; i++) {
            x[i] = stdIn.nextInt();
        }
        quickSort(x, 0, nx-1);
        for (int i : x) {
            System.out.println(i);
        }
    }


}
