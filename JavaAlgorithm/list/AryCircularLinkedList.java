package list;

import java.util.Comparator;

public class AryCircularLinkedList<E> {

    class Node<E> {

        private E data;
        private int next;
        private int dnext;

        void set(E data, int next) {
            this.data = data;
            this.next = next;
        }
    }

    private Node<E>[] n;
    private int size;
    private int max;
    private int head;
    private int tail;
    private int crnt;
    private int deleted;
    private static final int NULL = -1;

    public AryCircularLinkedList(int capacity) {
        head = crnt = tail = max = deleted = NULL;
        try {
            n = new Node[capacity];
            for (int i = 0; i < capacity; i++) {
                n[i] = new Node<E>();
            }
            size = capacity;
        } catch (OutOfMemoryError e) {
            size = 0;
        }
    }

    private int getInsertIndex() {
        if (deleted == NULL) {
            if (max < size) {
                return ++max;
            } else {
                return NULL;
            }
        } else {
            int rec = deleted;
            deleted = n[rec].dnext;
            return rec;
        }
    }

    private void deleteIndex(int idx) {
        if (deleted == NULL) {
            deleted = idx;
            n[idx].dnext = NULL;
        } else {
            int rec = deleted;
            deleted = idx;
            n[idx].dnext = rec;
        }
    }

    public E search(E obj, Comparator<? super E> c) {
        int ptr = head;
        do {
            if (c.compare(obj, n[ptr].data) == 0) {
                crnt = ptr;
                return n[ptr].data;
            }
            ptr = n[ptr].next;
        } while (ptr != head);
        return null;
    }

    public void addFirst(E obj) {
        if (head == NULL) {
            int rec = getInsertIndex();
            if (rec != NULL) {
                head = crnt = tail = rec;
                n[head].set(obj, rec);
            }
        } else {
            int ptr = head;
            int rec = getInsertIndex();
            if (rec != NULL) {
                head = crnt = rec;
                n[head].set(obj, ptr);
                n[tail].next = head;
            }
        }
    }

    public void addLast(E obj) {
        if (head == NULL) {
            addFirst(obj);
        } else {
            int rec = getInsertIndex();
            if (rec != NULL) {
                n[tail].next = crnt = rec;
                n[rec].set(obj, head);
                tail = rec;
            }
        }
    }

    public void removeFirst() {
        if (head != NULL) {
            if (head == tail) {
                deleteIndex(head);
                head = tail = crnt = NULL;
            } else {
                int ptr = n[head].next;
                deleteIndex(head);
                head = crnt = ptr;
                n[tail].next = head;
            }
        }
    }

    public void removeLast() {
        if (head != NULL) {
            if (head == tail) {
                removeFirst();
            } else {
                int ptr = head;
                int pre = head;

                while (n[ptr].next != tail) {
                    pre = ptr;
                    ptr = n[ptr].next;
                }
                n[pre].next = head;
                deleteIndex(ptr);
                tail = crnt = pre;
            }
        }
    }

    public void remove(int p) {
        if (head != NULL) {
            if (p == head) {
                removeFirst();
            } else if (p == tail) {
                removeLast();
            } else {
                int ptr = head;
                while (n[ptr].next != p) {
                    ptr = n[ptr].next;
                    if (ptr == head) return;
                }
                n[ptr].next = n[p].next;
                deleteIndex(p);
                crnt = ptr;
            }
        }
    }

    public void removeCurrentNode() {
        remove(crnt);
    }

    public void clear() {
        while (head != NULL) {
            removeFirst();
        }
        crnt = NULL;
    }

    public boolean next() {
        if (crnt == NULL || n[crnt].next == NULL) {
            return false;
        } else {
            crnt = n[crnt].next;
            return true;
        }
    }

    public void printCurrentNode() {
        if (crnt == NULL) {
            System.out.println("노드 없음");
        } else {
            System.out.println(n[crnt].data);
        }
    }

    public void dump() {
        if (head != NULL) {
            int ptr = head;
            do {
                System.out.println(n[ptr].data);
                ptr = n[ptr].next;
            } while (ptr != head);
        }
    }

    public void purge(Comparator<? super E> c) {
        if (head == NULL) {
            return;
        }
        int ptr = head;
        do {
            int count = 0;
            int ptr2 = ptr;
            int pre = ptr;

            while (n[pre].next != head) {
                ptr2 = n[pre].next;
                if (c.compare(n[ptr].data, n[ptr2].data) == 0) {
                    remove(ptr2);
                    count++;
                } else {
                    pre = ptr2;
                }
            }
            if (count == 0) {
                ptr = n[ptr].next;
            } else {
                int tmp = n[ptr].next;
                remove(ptr);
                ptr = tmp;
            }
        } while (n[ptr].next != head);
        crnt = head;
    }

    public E retrieve(int k) {
        if (head != NULL) {
            int ptr = head;
            int count = 0;

            while (count < k) {
                ptr = n[ptr].next;
                count++;
                if (ptr == head) return null;
            }
            return n[ptr].data;
        }
        return null;
    }

}
