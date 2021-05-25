package tree;

import java.util.Comparator;

public class BinTree<K, V> {

    static class Node<K, V> {
        private K key;
        private V data;
        private Node<K, V> left;
        private Node<K, V> right;

        Node(K key, V data, Node<K, V> left, Node<K, V> right) {
            this.key = key;
            this.data = data;
            this.left = left;
            this.right = right;
        }
        K getKey() {
            return key;
        }
        V getValue() {
            return data;
        }
        void print() {
            System.out.println(data);
        }
    }

    private Node<K, V> root;
    private Comparator<? super K> comparator = null;

    public BinTree() {
        root = null;
    }

    public BinTree(Comparator<? super K> c) {
        this();
        comparator = c;
    }

    // 2개의 키값을 비교하는 메서드. comparator가 따로 없는 경우(기본형 int나 string인 경우)도 커버함.
    private int comp(K key1, K key2) {
        return (comparator == null) ? ((Comparable<K>) key1).compareTo(key2) : comparator.compare(key1, key2);
    }

    public V search(K key) {
        Node<K, V> p = root;
        while (true) {
            if (p == null) {
                return null;
            }
            int cond = comp(key, p.getKey());
            if (cond == 0) {
                return p.getValue(); // 검색 성공 (키가 같음)
            } else if (cond < 0) {
                p = p.left; // 키 값이 더 작을 경우
            } else {
                p = p.right;
            }
        }
    }

    private void addNode(Node<K, V> node, K key, V data) {
        int cond = comp(key, node.getKey());
        if (cond == 0) {
            return; // key가 이미 이진 검색 트리에 존재함
        } else if (cond < 0) {
            if (node.left == null) {
                node.left = new Node<K, V>(key, data, null, null);
            } else {
                addNode(node.left, key, data); // 왼쪽 서브트리로 이동
            }
        } else { // 키값이 더 큰 경우
            if (node.right == null) {
                node.right = new Node<K, V>(key, data, null, null);
            } else {
                addNode(node.right, key, data); // 오른쪽 서브트리로 이동
            }
        }
    }

    public void add(K key, V data) {
        if (root == null) {
            root = new Node<K, V>(key, data, null, null);
        } else {
            addNode(root, key, data); // root를 서브트리로 하는 트리에 키, 데이터를 가진 노드를 삽입
        }
    }

    public boolean remove(K key) {
        Node<K, V> p = root;
        Node<K, V> parent = null; // 스캔중인 노드의 부모 노드
        boolean isLeftChild = true; // p가 왼쪽 자식 노드인가를 체크하는 변수

        while (true) { // 스캔 과정
            if (p == null) {
                return false; // root가 없을 때
            }
            int cond = comp(key, p.getKey());
            if (cond == 0) {
                break; // 검색 성공
            } else {
                parent = p; // 가지로 내려가기 이전에 부모를 설정한다.
                if (cond < 0) {
                    isLeftChild = true;
                    p = p.left;
                } else {
                    isLeftChild = false;
                    p = p.right;
                }
            }
        } // 찾은 이후 상황
        if (p.left == null) { // 왼쪽 서브트리가 없는 상황
            if (p == root) { // 찾은 p가 루트노드일 때
                root = p.right;  // 루트만 바꿔줌
            } else if (isLeftChild) {
                parent.left = p.right;
            } else {
                parent.right = p.right;
            }
        } else if (p.right == null) { // 오른쪽 서브트리가 없을 때
            if (p == root) {
                root = p.left; // 루트라면
            } else if (isLeftChild) {
                parent.left = p.left;
            } else {
                parent.right = p.left;
            }
        } else { // 둘다 존재 (새끼가 왼, 오른쪽 다 존재) --> 왼쪽 서브트리중 가장 큰 값을 옮겨와야함.
            parent = p;
            Node<K, V> left = p.left;
            isLeftChild = true;
            while (left.right != null) {
                parent = left;
                left = left.right;
                isLeftChild = false;
            }
            p.key = left.key;
            p.data = left.data;
            if (isLeftChild) {
                parent.left = left.left;
            } else {
                parent.right = left.left;
            }
        }
        return true;
    }

    private void printSubTree(Node node) { // 오름차순 출력 --> 중위 순회 방법 사용
        if (node != null) {
            printSubTree(node.left);
            System.out.println(node.key + " " + node.data);
            printSubTree(node.right);
        }
    }

    public void print() {
        printSubTree(root);
    }
}
