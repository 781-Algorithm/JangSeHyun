package list;

import java.util.Comparator;

public class LinkedList<E> {

     private class Node<E> {

        private E data; // 데이터
        private Node<E> next; // 뒤쪽 포인터 이 값은 실제적인 값이 아니라 포인터의 역할을 하고 있는 것임!!

        Node(E data, Node<E> next) {
            this.data = data;
            this.next = next;
        }
    }

    private Node<E> head; // 머리 노드
    private Node<E> crnt; // 선택 노드(현재 노드)

    public LinkedList() {
        head = crnt = null; // head가 null이면 연결리스트가 비어있는 것.
    }

    public E search(E obj, Comparator<? super E> c) { // Comparator를 직접 구현해야 함! (compare 메서드 오버라이딩)

        Node<E> ptr = head; // 가장먼저 head로 초기화 시킴.

        while (ptr != null) { // next의 값이 null이 될때 까지!
            if (c.compare(obj, ptr.data) == 0) { // 검색이 성공함
                crnt = ptr;
                return ptr.data; // 검색이 성공했을 때, crnt는 검색한 노드에 앉아있음.
            }
            ptr = ptr.next;
        }
        return null;
    }

    // 머리에 노드 삽입
    public void addFirst(E obj) {
        Node<E> ptr = head; // 먼저 현재 포인터를 헤드로 옮기고
        head = crnt = new Node<E>(obj, ptr); // 새로 추가 될 노드의 next 값을 head로 바꾸고 이를 head와 crnt 값으로 사용.
    }

    public void addLast(E obj) {
        if (head == null) {
            addFirst(obj); // 리스트가 비어있다면 head로 넣어두기
        } else {
            Node<E> ptr = head;
            while (ptr.next != null) {
                ptr = ptr.next;
            }
            ptr.next = crnt = new Node<E>(obj, null); // 현재노드 값 마찬가지로 여기로 옮겨준다.
        }
    }

    public void removeFirst() {
        if (head != null) {
            head = crnt = head.next;
        }
    }

    public void removeLast() {
        if (head != null) {
            if (head.next == null) {
                removeFirst(); // 노드가 한개만 있는 경우에는 머리노드 삭제
            } else {
                Node<E> ptr = head;
                Node<E> pre = head; // 스캔 중인 노드의 앞쪽 노드가 필요하다. 당연히!

                while (ptr.next != null) {
                    pre = ptr;
                    ptr = ptr.next; // 종료된다면 ptr은 꼬리노드를 가리키고, pre는 꼬리노드의 이전 노드를 가리킨다.
                }
                crnt = pre; // LinkedList의 포인터를 새로운 꼬리노드로 옮겨두고
                pre.next = null; // 삭제 garbage collecting에 따라 기존의 노드는 지워진다.
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
                    if (ptr == null) return; // p가 리스트에 존재하지 않음!
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
        if (crnt == null || crnt.next == null) {
            return false; // 이동할 수 없음. (마지막 노드거나 리스트가 없음)
        }
        crnt = crnt.next;
        return true;
    }

    public void printCurrentNode() { // 현재 선택 노드의 데이터를 출력
        if (crnt == null) {
            System.out.println("선택한 노드가 없습니다");
        } else {
            System.out.println(crnt.data);
        }
    }

    public void dump() { // 모든 노드 데이터를 출력하기
        Node<E> ptr = head;
        while (ptr != null) {
            System.out.println(ptr.data);
            ptr = ptr.next;
        }
    }

    // Practice 1
    public void purge(Comparator<? super E> c) {

        Node<E> ptr = head;
        while (ptr != null) {
            int count = 0;
            Node<E> ptr2;
            Node<E> pre = ptr;

            while (pre.next != null) {
                ptr2 = pre.next;
                if (c.compare(ptr.data, ptr2.data) == 0) {
                    pre.next = ptr2.next;
                    count++;
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

    // Practice 2
    public E retrieve(int n) {

        if (head != null) {
            int cnt = 0;
            Node<E> ptr = head;
            while (cnt < n) {
                cnt++;
                ptr = ptr.next;
                if (ptr == null) {
                    return null;
                }
            }
            crnt = ptr;
            return ptr.data;
        }
        return null;
    }


}
