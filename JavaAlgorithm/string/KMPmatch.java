package string;
// https://www.youtube.com/watch?v=UcjK_k5PLHI
public class KMPmatch { // 시간 복잡도 O(n)

    static int kmpMatch(String txt, String pat) {
        int pt = 1; // 1부터 시작하는 것에 주의 (한칸씩 밀리게끔 만들어짐)
        int pp = 0;
        int[] skip = new int[pat.length() + 1]; // 건너 뛰기용 표 왜 한칸씩 밀리게끔 설게했을까? (*) 때문이다.

        skip[pt] = 0;
        while (pt != pat.length()) {
            if (pat.charAt(pt) == pat.charAt(pp)) {
                skip[++pt] = ++pp;
            } else if (pp == 0) {
                skip[++pt] = pp;
            } else {
                pp = skip[pp]; // (*) 이게 뭔가 훨 깔끔해 보이긴 함. 아니였으면 pp = skip[pp-1]이 되어야한다.
            }
        }

        pt = pp = 0;
        while (pt != txt.length() && pp != pat.length()) {
            if (txt.charAt(pt) == pat.charAt(pp)) {
                pt++;
                pp++; // 매칭이 되면 쭉쭉 나감
            } else if (pp == 0) {
                pt++; // 아얘 처음부터 틀린 경우에는 전체 포인터만 한칸 이동시킴
            } else {
                pp = skip[pp]; // 중간에 틀렸다면 pp를 테이블을 이용해 이동시킨다.
            }
        }
        if (pp == pat.length()) {
            return pt - pp;
        }
        return -1;
    }
}
