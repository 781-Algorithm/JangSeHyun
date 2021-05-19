package string;

import java.util.Scanner;

public class BruteForceMatch {

    static int bfMatch(String txt, String pat) {
        int pt = 0;
        int pp = 0;

        while (pt != txt.length() && pp != pat.length()) {
            if (txt.charAt(pt) == pat.charAt(pp)) {
                pt++;
                pp++;
            } else {
                pt = pt - pp + 1;
                pp = 0;
            }
        }
        if (pp == pat.length()) {
            return pt - pp;
        }
        return -1;
    }

    static int bfMatchLast(String txt, String pat) {
        int pt = txt.length() - pat.length();
        int pp = 0;
        while (pt >= 0 && pp != pat.length()) {
            if (txt.charAt(pt) == pat.charAt(pp)) {
                pt++;
                pp++;
            } else {
                pt = pt - pp - 1;
                pp = 0;
            }
        }
        if (pp == pat.length()) {
            return pt - pp;
        }
        return -1;
    }

    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);
        String txt = stdIn.next();
        String pat = stdIn.next();
        int idx = bfMatchLast(txt, pat);
        System.out.println(idx);

        if (idx != -1) {
            int len = 0;
            for (int i = 0; i < idx; i++) {
                len += txt.substring(i, i + 1).getBytes().length;
            }
            len += pat.length();
        }
    }
}
