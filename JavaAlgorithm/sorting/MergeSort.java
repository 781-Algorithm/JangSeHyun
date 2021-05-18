package sorting;

import java.util.Scanner;

public class MergeSort {

    static int[] buff; // 작업용 배열

    static void __mergeSort(int[] a, int left, int right) {
        if (left < right) {
            int i;
            int mid = (left + right) / 2;
            int p = 0; // buff의 용량 체크
            int j = 0; // 실제 buff내의 포인터
            int k = left; // a의 포인터

            __mergeSort(a, left, mid); // 배열의 앞부분
            __mergeSort(a, mid + 1, right); // 배열의 뒷부분

            for (i = left; i <= mid; i++) {
                buff[p++] = a[i]; // 앞 배열을 buff에 복사
            }

            while (i <= right && j < p) {
                a[k++] = (buff[j] <= a[i]) ? buff[j++] : a[i++];
                // 병합시작. buff에 복사된 앞 배열과 mid+1로부터 시작되는 앞 배열을 병합.
            }

            while (j < p) {
                a[k++] = buff[j++];
            }
        }
    }

    static void mergeSort(int[] a, int n) {
        buff = new int[n];
        __mergeSort(a, 0, n - 1);
        buff = null;
    }

    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);
        int nx = stdIn.nextInt();
        int[] x = new int[nx];
        for (int i = 0; i < nx; i++) {
            x[i] = stdIn.nextInt();
        }

        mergeSort(x, nx);
        for (int i : x) {
            System.out.println(i);
        }
    }
}
