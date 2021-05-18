package set;

public class IntSortedSet {

    private int max;
    private int num;
    private int[] set;

    public IntSortedSet(int capacity) {
        num = 0;
        max = capacity;
        try {
            set = new int[max];
        } catch (OutOfMemoryError e) {
            max = 0;
        }
    }

    public int indexOf(int n) {
        int pl = 0;
        int pr = num - 1;

        do {
            int pc = (pl + pr) / 2;
            if (set[pc] == n) {
                return pc;
            } else if (set[pc] < n) {
                pl = pc + 1;
            } else {
                pr = pc - 1;
            }
        } while (pl <= pr);
        return -pl - 1;
    }

    public boolean contains(int num) {
        return indexOf(num) >= 0;
    }

    public boolean add(int n) {
        int idx;
        if (num >= max || (idx = indexOf(n)) >= 0) {
            return false;
        }
        else{
            num++;
            for (int i = num-1; i > idx; i--) {
                set[i] = set[i - 1];
            }
            set[idx] = n;
        }
        return true;
    }

    public boolean remove(int n) {
        int idx;
        if (num <= 0 || (idx = indexOf(n)) < 0) {
            return false;
        }
        else{
            num--;
            for (int i = idx; i < num; i++) {
                set[i] = set[i + 1];
            }
            return true;
        }
    }

}
