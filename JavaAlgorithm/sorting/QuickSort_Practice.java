package sorting;

import java.util.Scanner;

public class QuickSort_Practice {

    static void swap(int[] a, int idx1, int idx2) {
        int t = a[idx1];
        a[idx1] = a[idx2];
        a[idx2] = t;
    }

    static void insertionSort(int[] a, int left, int right) {
        for (int i = left + 1; i <= right; i++) {
            int j;
            int temp = a[i];
            for (j = i; j > left && a[j-1] > temp; j--) {
                a[j] = a[j-1];
            }
            a[j] = temp;
        }
    }

    // 요소의 개수가 적은 그룹을 먼저 나누는 방식으로 구현
    static void quest12(int[] a, int left, int right) {

        int pl = left;
        int pr = right;
        int x = a[(pl + pr) / 2];

        int left_num = 0;
        int right_num = 0;

        do {
            while (a[pl] < x) pl++;
            while (a[pr] > x) pr--;
            if (pl <= pr) {
                swap(a, pl++, pr--);
            }
        } while (pl <= pr);

        left_num = pr - left;
        right_num = right - pl;

        if (left_num > right_num) {
            quest12(a,left,pr);
            if (right_num > 0) quest12(a,pl,right);
        }
        else {
            if(right_num > 0) quest12(a,pl,right);
            if(left_num > 0) quest12(a,left,pr);
        }
    }

    // 개수가 9개 이하면 삽입정렬로 가기
    void quest13(int[] a, int left, int right) {
        if (left - right < 9) {
            insertionSort(a,left,right);
        }
        else {
            int pl = left;
            int pr = right;
            int x = a[(pl + pr) / 2];

            int left_num = 0;
            int right_num = 0;

            do {
                while (a[pl] < x) pl++;
                while (a[pr] > x) pr--;
                if (pl <= pr) {
                    swap(a, pl++, pr--);
                }
            } while (pl <= pr);

            left_num = pr - left;
            right_num = right - pl;

            if (left_num > right_num) {
                quest12(a, left, pr);
                if (right_num > 0) quest12(a, pl, right);
            } else {
                if (right_num > 0) quest12(a, pl, right);
                if (left_num > 0) quest12(a, left, pr);
            }
        }
    }

    static int swap3Elem(int[] a, int x, int y, int z) {
        if (a[x] > a[y]) {
            swap(a,x,y);
        }
        if (a[y] > a[z]) {
            swap(a,y,z);
        }
        if (a[x] > a[z]) {
            swap(a, x, z);
        }
        return y;
    }

    // 피벗 선택방법을 달리하여 구현
    static void quest15(int[] a, int left, int right) {

        if (left - right < 9) {
            insertionSort(a,left,right);
        }
        else {
            int pl = left;
            int pr = right;
            int mid = (pl + pr) / 2;

            int p_idx = swap3Elem(a, pl, mid, pr);
            int x = a[p_idx];

            swap(a,p_idx,right-1);
            pl++;
            pr--;

            int left_num = 0;
            int right_num = 0;

            do {
                while (a[pl] < x) pl++;
                while (a[pr] > x) pr--;
                if (pl <= pr) {
                    swap(a, pl++, pr--);
                }
            } while (pl <= pr);

            left_num = pr - left;
            right_num = right - pl;

            if (left_num > right_num) {
                quest12(a, left, pr);
                if (right_num > 0) quest12(a, pl, right);
            } else {
                if (right_num > 0) quest12(a, pl, right);
                if (left_num > 0) quest12(a, left, pr);
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

        quest12(x, 0, nx - 1); // 배열 x를 퀵정렬

        for (int i : x) {
            System.out.println(i);
        }

    }
}
