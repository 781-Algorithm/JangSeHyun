package sorting;

import java.util.Scanner;

public class Fsort {

    static void fSort(int[] a, int n, int max) {
        int[] f = new int[max + 1];
        int[] b = new int[n];

        for (int i = 0; i < n; i++) f[a[i]]++; // 도수에 집어넣기
        for (int i = 1; i <= max; i++) f[i] += f[i - 1]; // 누적 도수
        for (int i = n - 1; i >= 0; i--) b[--f[a[i]]] = a[i]; // 목적 배열 만들기
        for (int i = 0; i < n; i++) b[i] = a[i];
    }

    static void fSort2(int[] a, int n, int min, int max) {
        int[] f = new int[max + 1 - min];
        int[] b = new int[n];

        for (int i = 0; i < n; i++) f[a[i] - min]++;
        for (int i = 1; i <= max - min; i++) f[i] += f[i - 1];
        for (int i = n - 1; i >= 0; i--) b[--f[a[i] - min]] = a[i];
        for (int i = 0; i < n; i++) b[i] = a[i];

    }

    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);
        int nx = stdIn.nextInt();
        int[] x = new int[nx];

        for (int i = 0; i < nx; i++) {
            x[i] = stdIn.nextInt();
        }

        for (int i : x) {
            System.out.println("i = " + i);
        }
    }
}
