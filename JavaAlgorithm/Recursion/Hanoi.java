package Recursion;

import java.util.Scanner;

public class Hanoi {

    static void move(int no, int x, int y) { // 원반 개수, 시작기둥 넘버, 목표기둥 넘버 ( 1, 2, 3번 기둥이 있다고 가정)
        if (no > 1) {
            move(no - 1, x, 6 - x - y);
        }
        System.out.println("원반 "+no+" 개를 "+x+" 에서 "+y+" 로 옮김.");

        if (no > 1) {
            move(no - 1, 6 - x - y, y);
        }
    }

    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);
        int n = stdIn.nextInt(); // 원반 개수
        move(n, 1, 3);
        // https://www.acmicpc.net/problem/11729
    }
}
