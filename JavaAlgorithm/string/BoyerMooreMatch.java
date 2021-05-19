package string;

import java.util.Scanner;

public class BoyerMooreMatch {

    static int bmMatch(String txt, String pat) {
        int pt;
        int pp;
        int txtLen = txt.length();
        int patLen = pat.length();
        int[] skip = new int[Character.MAX_VALUE + 1]; // 패턴에 존재하는 모든 문자의 옮길 크기를 계산하고 저장해야 하기에!

        // 건너뛰기 표 만들기
        for (pt = 0; pt <= Character.MAX_VALUE; pt++) {
            skip[pt] = patLen; // 초기화
        }
        for (pt = 0; pt < patLen - 1; pt++) {
            skip[pat.charAt(pt)] = patLen - pt - 1; // 있다면 얼마만큼 이동 시킬 것인지! ( 뒤에서 부터 몇칸째에 있는지를 기록 )
        }

        while (pt < txtLen) {
            pp = patLen - 1;
            while (txt.charAt(pt) == pat.charAt(pp)) {
                if (pp == 0) {
                    return pt; // 값을 찾았다면
                }
                pp--;
                pt--;
            }
            pt += Math.max(skip[txt.charAt(pt)], patLen - pp); // 얼마만큼 건너 뛸 것인지? max를 쓴 이유는 negative shift를 막기 위해서
        }
        return -1;
    }

    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);
        String txt = stdIn.next();
        String pat = stdIn.next();
        System.out.println(bmMatch(txt, pat));
    }
}
