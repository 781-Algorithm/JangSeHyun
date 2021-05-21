package list;

import java.util.Comparator;

public class LinkedListT<E> {

    private class Node<E> {

        private E data; // 데이터
        private Node<E> next; // 뒤쪽 포인터 이 값은 실제적인 값이 아니라 포인터의 역할을 하고 있는 것임!!

        Node(E data, Node<E> next) {
            this.data = data;
            this.next = next;
        }
    }

    private Node<E> head;
    private Node<E> tail;
    private Node<E> crnt;

    public LinkedListT() {
        head = tail = crnt = null;
    }

    private E search(E obj, Comparator<? super E> c) {
        Node<E> ptr = head;
        while (ptr != null) {
            if (c.compare(ptr.data, obj) == 0) {
                crnt = ptr;
                return ptr.data;
            }
            ptr = ptr.next;
        }
        return null;
    }

    private void addFirst(E obj) {
        Node<E> ptr = head;
        head = crnt = new Node<>(obj, ptr);
        if (tail == null) {
            tail = crnt;
        }
    }

    private void addLast(E obj) {
        if (head == null) {
            addFirst(obj);
        } else {
            tail.next = crnt = new Node<E>(obj, null);
            tail = crnt;
        }
    }

    public void removeFirst() {
        if (head != null) {
            if (head == tail) {
                tail = head.next;
            }
            head = crnt = head.next;
        }
    }

    public void removeLast() {
        if (head != null) {
            if (head == tail) {
                removeFirst();
            } else {
                Node<E> ptr = head;
                Node<E> pre = head;

                while (ptr.next != null) {
                    pre = ptr;
                    ptr = ptr.next;
                }
                pre.next = null;
                tail = crnt = pre;
            }
        }
    }

    public void remove(Node p) {
        if (head != null) {
            if (head == tail) {
                removeFirst();
            } else {
                if (p == tail) {
                    removeLast();
                } else {
                    Node<E> ptr = head;
                    while (ptr.next != p) {
                        ptr = ptr.next;
                        if (ptr ==null) return;
                    }
                    ptr.next = p.next;
                    crnt = ptr;
                }
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
        if (crnt == tail) {
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
        while (ptr != null) {
            System.out.println(ptr.data);
            ptr = ptr.next;
        }
    }

    public void purge(Comparator<? super E> c) {
        Node<E> ptr = head;
        while (ptr != null) {
            Node<E> ptr2 = ptr;
            Node<E> pre = ptr;
            int count = 0;
            while (pre.next != null) {
                ptr2 = pre.next;
                if (c.compare(ptr.data, ptr2.data) == 0) {
                    count++;
                    pre.next = ptr2.next;
                } else {
                    pre = ptr2;
                }
            }
            if (count == 0) {
                ptr = ptr.next;
            } else {
                Node<E> temp = ptr;
                remove(ptr);
                ptr = temp.next;
            }
        }
        crnt = head;
    }

    public E retrieve(int n) {
        if(n>=0){
            Node<E> ptr = head;
            int count = 0;
            while (count < n) {
                count++;
                ptr = ptr.next;
                if (ptr == null) return null;
            }
            crnt = ptr;
            return ptr.data;
        }
        return null;
    }


}
