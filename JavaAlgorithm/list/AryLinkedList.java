package list;

import java.util.Comparator;

// 연결 리스트 클래스(배열 커서 버전)
public class AryLinkedList<E> {

    class Node<E> {
        private E data;
        private int next; // 리스트의 뒤쪽 포인터
        private int dnext; // free 리스트의 뒤쪽 포인터

        void set(E data, int next) {
            this.data = data;
            this.next = next;
        }
    }

    private Node<E>[] n;
    private int size; // 리스트 본체의 사이즈
    private int max; // 사용중인 꼬리 record
    private int head;
    private int crnt;
    private int deleted; // free 리스트의 머리 노드
    private static final int NULL = -1; // 다음 노드가 없거나 리스트가 가득 찰 때

    public AryLinkedList(int capacity) {
        head = crnt = max = deleted = NULL;
        try {
            n = new Node[capacity];
            for (int i = 0; i < capacity; i++) {
                n[i] = new Node<E>();
            }
            size = capacity;
        } catch (OutOfMemoryError error) {
            size = 0;
        }
    }

    // 다음의 삽입하는 record의 인덱스를 구하기
    private int getInsertIndex() {
        if (deleted == NULL) { // 삭제할 레코드가 없음
            if (max < size) {
                return ++max; // 새로운 record를 사용
            } else {
                return NULL; // 용량이 over
            }
        } else {
            int rec = deleted; // free list에서
            deleted = n[rec].dnext; // 머리 rec를 꺼낸다
            return rec;
        }
    }

    // record idx를 free 리스트에 등록하기
    private void deleteIndex(int idx) {
        if (deleted == NULL) { // 삭제할 레코드가 없을 때
            deleted = idx; // idx를 free 리스트의
            n[idx].dnext = NULL; // 머리에 등록한다
        } else {
            int rec = deleted; // idx를 free 리스트의
            deleted = idx; // 머리에 삽입하기
            n[idx].dnext = rec;
        }
    }

    public E search(E obj, Comparator<? super E> c) {
        int ptr = head;
        while (ptr != NULL) {
            if (c.compare(obj, n[ptr].data) == 0) {
                crnt = ptr;
                return n[ptr].data;
            }
            ptr = n[ptr].next;
        }
        return null;
    }

    public void addFirst(E obj) {
        int ptr = head;
        int rec = getInsertIndex();
        if (rec != NULL) {
            head = crnt = rec;
            n[head].set(obj, ptr);
        }
    }

    public void addLast(E obj) {
        if (head == NULL) {
            addFirst(obj);
        } else {
            int ptr = head;
            while (n[ptr].next != NULL)
                ptr = n[ptr].next;

            int rec = getInsertIndex();
            if (rec != NULL) {
                n[ptr].next = crnt = rec;
                n[rec].set(obj, NULL);
            }

        }
    }

    public void removeFirst() {
        if (head != NULL) {
            int ptr = n[head].next;
            deleteIndex(head);
            head = crnt = ptr;
        }
    }

    public void removeLast() {
        if (head != NULL) {
            if (n[head].next == NULL) {
                removeFirst();
            } else {
                int ptr = head;
                int pre = head;
                while (n[ptr].next != NULL) {
                    pre = ptr;
                    ptr = n[ptr].next;
                }
                n[pre].next = NULL;
                deleteIndex(ptr);
                crnt = pre;
            }
        }
    }

    public void remove(int p) { // record p를 삭제하는 것
        if (head != NULL) {
            if (p == head) {
                removeFirst();
            } else {
                int ptr = head;
                while (n[ptr].next != p) {
                    ptr = n[ptr].next;
                    if (ptr == NULL) return;
                }
                n[ptr].next = NULL;
                deleteIndex(p);
                n[ptr].next = n[p].next;
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
        if (crnt==NULL || n[crnt].next == NULL) return false;
        crnt = n[crnt].next;
        return true;
    }

    public void printCurrentNode() {
        if (crnt == NULL) {
            System.out.println("선택 노드가 없습니다");
        } else {
            System.out.println(n[crnt].data);
        }
    }

    public void dump() {
        int ptr = head;
        while (ptr != NULL) {
            System.out.println(n[ptr].data);
            ptr = n[ptr].next;
        }
    }



}
