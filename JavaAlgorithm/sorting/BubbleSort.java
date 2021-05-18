package sorting;

import java.util.Scanner;

public class BubbleSort {

    static void swap(int[] a, int idx1, int idx2) {
        int t = a[idx1];
        a[idx1] = a[idx2];
        a[idx2] = t;
    }
    // 정석 방향 (맨 앞부터 채우기)
    static void bubbleSort(int[] a, int n) {
        for (int i = 0; i < n-1; i++) {
            for (int j = n - 1; j > i; j--) {
                if (a[j - 1] > a[j]) {
                    swap(a, j - 1, j);
                }
            }
        }
    }

    // 방향을 반대로
    static void bubbleSort_reverse(int[] a, int n) {
        for (int i = n - 1; i > 0; i--) {
            for (int j = 0; j < i; j++) {
                if (a[j] > a[j + 1]) {
                    swap(a, j, j+1);
                }
            }
        }
    }

    // Version 2
    static void bubbleSort2(int[] a, int n) {

        for (int i = 0; i < n - 1; i++) {
            int cnt = 0;
            for (int j = n - 1; j > i; j--) {
                if (a[j - 1] > a[j]) {
                    swap(a, j - 1, j);
                    cnt += 1;
                }
            }
            if (cnt == 0) {
                break;
            }

        }
    }

    // Version 3
    static void bubbleSort3(int[] a, int n) {
        int k = 0; // a[k]보다 앞쪽은 정렬이 끝이 난 상태
        while (k < n - 1) {
            int last = n - 1; // 마지막으로 요소를 교환한 위치
            for (int j = n - 1; j > k; j--) {
                if (a[j - 1] > a[j]) {
                    swap(a, j - 1, j);
                    last = j;
                }
            }
            k = last;
        }
    }

    static void bubbleSort3_reverse(int[] a, int n) {
        int k = n - 1;
        while (k > 0) {
            int last = 0;
            for (int j = 0; j < k; j++) {
                if (a[j] > a[j + 1]) {
                    swap(a, j, j + 1);
                    last = j;
                }
            }
            k = last;
        }
    }

    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        int nx = stdIn.nextInt();
        int[] x = new int[nx];

        for (int i = 0; i < nx; i++) {
            x[i] = stdIn.nextInt();
        }

        bubbleSort3_reverse(x, nx);
        for (int i = 0; i < nx; i++) {
            System.out.println(x[i]);
        }

    }

}

