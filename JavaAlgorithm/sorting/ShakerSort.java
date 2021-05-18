package sorting;

import java.util.Scanner;

public class ShakerSort {

    static void swap(int[] a, int idx1, int idx2) {
        int t = a[idx1];
        a[idx1] = a[idx2];
        a[idx2] = t;
    }

    // bi-direction bubble sort
    static void shakerSort(int[] a, int n) {

        int left = 0;
        int right = n - 1;
        int last = right;

        while (left < right) {
            for (int j = right; j > left; j--) {
                if (a[j] < a[j - 1]) {
                    swap(a, j - 1, j);
                    last = j;
                }
            }
            left = last;

            for (int j = left; j < right; j++) {
                if (a[j] > a[j + 1]) {
                    swap(a, j + 1, j);
                    last = j;
                }
            }
            right = last;
        }

    }

    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);
        int nx = stdIn.nextInt();
        int[] x = new int[nx];

        for (int i = 0; i < nx; i++) {
            x[i] = stdIn.nextInt();
        }

        shakerSort(x, nx);
        for (int i = 0; i < nx; i++) {
            System.out.println(x[i]);
        }



    }
}
