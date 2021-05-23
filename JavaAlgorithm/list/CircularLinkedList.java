package list;

import java.util.Comparator;

public class CircularLinkedList<E> {

    class Node<E> {

        private E data;
        private Node<E> next;

        Node(E data, Node<E> next) {
            this.data = data;
            this.next = next;
        }
    }

    private Node<E> head;
    private Node<E> tail;
    private Node<E> crnt;

    public CircularLinkedList() {
        head = crnt = tail = null;
    }

    public E search(E obj, Comparator<? super E> c) {
        Node<E> ptr = head;

        if (head != null) {
            do {
                if (c.compare(obj, ptr.data) == 0) {
                    crnt = ptr;
                    return ptr.data;
                }
                ptr = ptr.next;
            } while (ptr != head);
        }
        return null;
    }

    public void addFirst(E obj) {
        if (head == null) {
            head = tail = crnt = new Node<E>(obj, null);
        } else {
            Node<E> ptr = head;
            head = crnt = new Node<E>(obj, ptr);
            tail.next = head;
        }
    }

    public void addLast(E obj) {
        if (head == null) {
            addFirst(obj);
        } else {
            crnt = tail.next = new Node<>(obj, head);
            tail = crnt;
        }
    }

    public void removeFirst() {
        if (head != null) {
            head = crnt = tail.next = head.next;
        }
    }

    public void removeLast() {
        if (head != null) {
            if (head.next == null) {
                removeFirst();
            } else {
                Node<E> ptr = head;
                while (ptr.next != tail) {
                    ptr = ptr.next;
                }
                tail = crnt = ptr;
                ptr.next = head;
            }
        }
    }

    public void remove(Node p) {
        if (head != null) {
            if (head == p) {
                removeFirst();
            } else {
                Node<E> ptr = head;
                while (ptr.next != p) {
                    ptr = ptr.next;
                    if (ptr == head) return;
                }
                ptr.next = p.next;
                crnt = ptr;
            }
        }
    }

    public void removeCurrentNode() {
        remove(crnt);
    }

    public void clear() {
        while (head != null) {
            removeFirst();
        }
        crnt = null;
    }

    public boolean next() {
        if (crnt == null || crnt.next == head) {
            return false;
        }
        crnt = crnt.next;
        return true;
    }

    public void printCurrentNode() {
        if (crnt == null) {
            System.out.println("선택한 노드가 없습니다");
        } else {
            System.out.println(crnt.data);
        }
    }

    public void dump() {
        Node<E> ptr = head;
        if (head != null) {
            do {
                System.out.println(ptr.data);
                ptr = ptr.next;
            } while (ptr != head);
        }

    }

    public void purge(Comparator<? super E> c) {
        Node<E> ptr = head;
        do {
            int count = 0;
            Node<E> ptr2 = ptr;
            Node<E> pre = ptr;
            while (pre.next != head) {
                ptr2 = pre.next;
                if (c.compare(ptr.data, ptr2.data) == 0) {
                    remove(ptr2);
                    count++;
                }
            }
            if (count == 0) {
                ptr = ptr.next;
            } else {
                Node<E> tmp = ptr;
                remove(ptr);
                ptr = tmp.next;
            }
        } while (ptr.next != head);
    }

    public E retrieve(int n) {
        if (head != null) {
            Node<E> ptr = head;

            while (n >= 0) {
                if (n-- == 0) {
                    crnt = ptr;
                    return (ptr.data); // 검색성공
                }
                ptr = ptr.next; // 다음 노드에 선택
                if (ptr == head)
                    break;
            }
        }
        return null;
    }
}
