package sorting;

import recursion.RecurX2;

public class Practice {

    static void swap(int[] a, int idx1, int idx2) {
        int t = a[idx1];
        a[idx1] = a[idx2];
        a[idx2] = t;
    }

    static void shellSort(int[] a, int n) {
        for (int h = n / 2; h > 0; h /= 2) {
            for (int i = h; i < n; i++) {
                int j;
                int temp = a[i];
                for (j = i - h; j >= 0 && a[j] > temp; j -= h) {
                    a[j + h] = a[j];
                }
                a[j + h] = temp;
            }
        }
    }

    static void quickSort(int[] a, int left, int right) {

        int pl = left;
        int pr = right;
        int x = a[(pl + pr) / 2];

        do {
            while (a[pl] < x) pl++;
            while (a[pr] > x) pr--;

            if (pl <= pr) {
                swap(a, pl, pr);
            }
        } while (pl <= pr);

        if (left < pl) {
            quickSort(a, left, pr); // 왼쪽 그룹 나누기
        }

        if (right > pr) {
            quickSort(a, pl, right); // 오른쪽 그룹 나누기
        }
    }

    static void quickSort_nonRecur(int[] a, int left, int right) {
        RecurX2.IntStack lstack = new RecurX2.IntStack(right - left + 1);
        RecurX2.IntStack rstack = new RecurX2.IntStack(right - left + 1);

        lstack.push(left);
        rstack.push(right);

        while (!lstack.isEmpty()) {
            int pl = left = lstack.pop();
            int pr = right = rstack.pop();
            int x = a[(pl + pr) / 2];

            do {
                while (a[pl] < x) pl++;
                while (a[pr] > x) pr--;

                if (pl <= pr) {
                    swap(a, pl, pr);
                }
            } while (pl <= pr);

            if (left < pr) {
                lstack.push(left);
                rstack.push(pr);
            }
            if (right > pl) {
                rstack.push(right);
                lstack.push(pl);
            }
        }
    }
}
