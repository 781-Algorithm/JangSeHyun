package boj;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

public class boj5670 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = "";
        while ((s = br.readLine()) != null) {
            int n = Integer.parseInt(s);
            Trie trie = new Trie();
            for (int i = 0; i < n; i++) {
                trie.insert(br.readLine());
            }
            trie.buttonCount(trie.head,0);
            System.out.printf("%.2f%n", trie.total / (double) n);
        }
    }
    static class Trie {

        Map<String, Map> head;
        double total = 0;

        Trie() {
            this.head = new HashMap<>();
        }

        void insert(String string) {
            Map<String, Map> cur = head;
            for (int i = 0; i < string.length(); i++) {
                String s = String.valueOf(string.charAt(i));
                if (!cur.containsKey(s)) {
                    cur.put(s, new HashMap<String, Map>());
                }
                cur = cur.get(s);
            }
            cur.put("FIN", new HashMap());
        }

        void buttonCount(Map<String, Map> cur, int count) {
            if (!cur.containsKey("FIN")) {
                if (cur.size() == 1) {
                    for (String s : cur.keySet()) {
                        if (cur == this.head) {
                            count += 1;
                        }
                        this.buttonCount(cur.get(s), count);
                    }
                } else {
                    for (String s : cur.keySet()) {
                        this.buttonCount(cur.get(s), count + 1);
                    }
                }
            } else {
                if (cur.size() == 1) {
                    this.total += count;
                } else {
                    this.total += count;
                    for (String s : cur.keySet()) {
                        if (!s.equals("FIN")) {
                            this.buttonCount(cur.get(s),count+1);
                        }
                    }
                }
            }
        }

    }

}
//https://www.acmicpc.net/source/28170583 참고해보기