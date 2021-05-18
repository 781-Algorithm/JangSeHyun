package sorting;

import java.util.Scanner;

public class HeapSort {

    static void swap(int[] a, int idx1, int idx2) {
        int t = a[idx1];
        a[idx1] = a[idx2];
        a[idx2] = t;
    }

    static void downHeap(int[] a, int left, int right) {
        int temp = a[left]; // 루트
        int child; // 큰 값을 가진 노드
        int parent; // 부모

        for (parent = left; parent < (right + 1) / 2; parent = child) {
            int cl = parent * 2 + 1; // 왼쪽 자식
            int cr = cl + 1; // 오른쪽 자식
            child = (cr <= right && a[cr] > a[cl]) ? cr : cl; // 큰 값을 가진 노드를 자식에 대입한다.
            if (temp >= a[child]) {
                break; // 지금 루트가 자식중 큰 것들보다 크다면 더이상 할 것 없음.
            }
            a[parent] = a[child]; // 그게 아니면 값을 바꿈
        }
        a[parent] = temp; // 그리고 원래 child의 위치에 루트 값을 넣기.
    }

    static void heapSort(int[] a, int n) {
        for (int i = (n - 1) / 2; i >= 0; i--) {
            downHeap(a, i, n - 1); // a[i] ~ a[n-1]을 힙으로 만들기 (초기 세팅)
        }
        for (int i = n - 1; i > 0; i--) {
            swap(a, 0, i); // 초기 세팅을 마치고 나면 가장 큰 원소가(루트) 맨 뒤로 가게 됨.
            downHeap(a,0,i-1); // a[0] ~ a[i-1]을 힙으로 만들기
        }
    }

    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);
        int nx = stdIn.nextInt();
        int[] x = new int[nx];

        for (int i = 0; i < nx; i++) {
            x[i] = stdIn.nextInt();
        }
        heapSort(x, nx);
        for (int i : x) {
            System.out.println(i);
        }
    }
}
