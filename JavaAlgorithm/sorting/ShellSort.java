package sorting;

import java.util.Scanner;

public class ShellSort {

    // Version 1
    static int shellSort(int[] a, int n) {
        int count = 0;
        for (int h = n / 2; h > 0; h /= 2) {
            for (int i = h; i < n; i++) {
                int j;
                int tmp = a[i];
                for (j = i - h; j >= 0 && a[j] > tmp; j -= h) {
                    a[j + h] = a[j];
                    count += 1;
                }
                a[j + h] = tmp;
                count += 1;
            }
        }
        return count; // 몇번 요소를 이동시켜야 하는지 리턴
    }

    // Version 2
    static int shellSort2(int[] a, int n) {
        int h;
        for (h = 1; h < n / 9; h = 3 * h + 1); // 가장 큰 h 값으로 초기화 시키기
        int count = 0;
        for (; h > 0; h /= 3) {
            for (int i = h; i < n; i++) {
                int j;
                int tmp = a[i];
                for (j = i - h; j >= 0 && a[j] > tmp; j-=h) {
                    a[j + h] = a[j];
                    count += 1;
                }
                a[j + h] = a[j];
                count += 1;
            }
        }
        return count; // 기존의 시간 복잡도 N^2를 N^1.25까지 줄인다.
    }



    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);
        int nx = stdIn.nextInt();
        int[] x = new int[nx];

        for (int i = 0; i < nx; i++) {
            x[i] = stdIn.nextInt();
        }

        shellSort(x, nx);
        for (int i : x) {
            System.out.println(i);
        }
    }
}
