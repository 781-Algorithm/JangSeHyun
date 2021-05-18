package set;

import java.util.Arrays;

public class IntSet {

    private int max; // 최대 개수
    private int num; // 실제 집합의 요소 수
    private int[] set;

    public IntSet(int capacity) {
        num = 0;
        max = capacity;
        try {
            set = new int[max];
        } catch (OutOfMemoryError e) {
            max = 0;
        }
    }

    public int capacity() {
        return max; // 집합의 최대 가수
    }

    public int size() {
        return num;
    }

    public int indexOf(int n) {
        for (int i = 0; i < num; i++) {
            if (set[i] == n) {
                return i;
            }
        }
        return -1;
    }

    public boolean contains(int n) {
        return (indexOf(n) != -1);
    }

    public boolean add(int n) {
        if (num >= max || contains(n)) {
            return false;
        }
        set[num++] = n;
        return true;
    }

    public boolean remove(int n) {
        int idx;
        if (num <= 0 || (idx = indexOf(n)) == -1) {
            return false;
        }
        set[idx] = set[--num]; // 마지막 요소를 삭제한 곳으로 옮기기 ! 여기가 핵심인듯.
        return true;
    }

    // 집합 s에 복사
    public void copyTo(IntSet s) {
        int n = (s.max < num) ? s.max : num; // 복사할 요소의 개수
        for (int i = 0; i < n; i++) {
            s.set[i] = set[i];
        }
        s.num = n;
    }

    // 집합 s를 복사
    public void copyFrom(IntSet s) {
        int n = (max < s.num) ? max : s.num;
        for (int i = 0; i < n; i++) {
            set[i] = s.set[i];
        }
        num = n;
    }

    public boolean eqaulTo(IntSet s) {
        if (num != s.num) {
            return false;
        }
        for (int i = 0; i < num; i++) {
            int j = 0;
            for (; j < s.num; j++) {
                if (set[i] == s.set[j]) {
                    break;
                }
            }
            if (j == s.num) {
                return false; // 똑같은 원소를 찾지 못함.
            }
        }
        return true;
    }

    public void unionOf(IntSet s1, IntSet s2) {
        copyFrom(s1);
        for (int i = 0; i < s2.num; i++) {
            add(s2.set[i]);
        }
    }

    @Override
    public String toString() {
        StringBuffer temp = new StringBuffer("{");
        for (int i = 0; i < num; i++) {
            temp.append(set[i]).append(" ");
        } // {a b c }와 같은 형식으로 바꾸기.
        temp.append("}");
        return temp.toString();
    }

    // Practice
    public boolean isEmpty() {
        return (num == 0);
    }

    public boolean isFull() {
        return (num == max);
    }

    public void clear() {
        num = 0;
    }

    public boolean union(IntSet s1) {
        boolean flag = false;
        for (int i = 0; i < s1.num; i++) {
            if (add(s1.set[i])){
                flag = true;
            }
        }
        return flag;
    }

    public boolean retain(IntSet s1) {
        boolean flag = false;
        for (int i = 0; i < num; i++) {
            if (!s1.contains(set[i])) {
                remove(set[i]);
                flag = true;
            }
        }
        return flag;
    }

    public boolean remove(IntSet s1) {
        boolean flag = false;
        for (int i = 0; i < num; i++) {
            if (s1.contains(set[i])) {
                remove(set[i]);
                flag = true;
            }
        }
        return flag;
    }

    public boolean isSubsetOf(IntSet s) {
        if (num > s.num) {
            return false;
        }
        for (int i = 0; i < num; i++) {
            if (!s.contains(set[i])) {
                return false;
            }
        }
        return true;
    }

    public boolean isProperSubsetOf(IntSet s) {
        if (num >= s.num) {
            return false;
        }
        for (int i = 0; i < num; i++) {
            if (!s.contains(set[i])) {
                return false;
            }
        }
        return true;
    }

    public void intersectionOf(IntSet s1, IntSet s2) {
        copyFrom(s1);
        for (int i = 0; i < num; i++) {
            if (!s2.contains(set[i])) {
                remove(set[i]);
            }
        }
    }

    public void differenceOf(IntSet s1, IntSet s2) {
        copyFrom(s1);
        for (int i = 0; i < num; i++) {
            if (s2.contains(set[i])) {
                remove(set[i]);
            }
        }
    }

    public static void main(String[] args) {
        IntSet s1 = new IntSet(20);
        IntSet s2 = new IntSet(20);
        IntSet s3 = new IntSet(20);

        s1.add(10);
        s1.add(15);
    }
}
