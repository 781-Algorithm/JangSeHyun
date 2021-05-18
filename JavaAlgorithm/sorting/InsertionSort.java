package sorting;

import java.util.Scanner;

public class InsertionSort {

    static void binaryInsertionSort(int[] a, int n) {

        for (int i = 1; i < n; i++) {
            int temp = a[i];

            int mid;
            int left = 0;
            int right = i;

            while (left < right) {
                mid = (left + right) / 2;
                if (a[mid] >= temp) {
                    right = mid;
                } else {
                    left = mid + 1;
                }
            }
            for (int j = i; j > right; j--) {
                a[j] = a[j - 1];
            }
            a[right] = temp;
        }
    }

    static void insertionSort(int[] a, int n) {
        for (int i = 1; i < n; i++) {
            int j;
            int temp = a[i];
            for (j = i; j > 0 && a[j - 1] > temp; j--) {
                a[j] = a[j - 1];
            }
            a[j] = temp;
        }
    }

    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);
        int n = stdIn.nextInt();
        int[] x = new int[n];

        for (int i = 0; i < n; i++) {
            x[i] = stdIn.nextInt();
        }

        binaryInsertionSort(x,n);

        for (int i : x) {
            System.out.println(i);
        }
    }
}
