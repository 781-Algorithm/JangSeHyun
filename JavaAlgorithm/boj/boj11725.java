package boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class boj11725 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        List<List<Integer>> tree = new ArrayList<>();
        List<Integer> parent = new ArrayList<>();

        for (int i = 0; i <= n; i++) {
            tree.add(new ArrayList<>());
            parent.add(0);
        }
        parent.set(1, 1);

        for (int i = 0; i < n - 1; i++) {
            int[] inputs = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            tree.get(inputs[0]).add(inputs[1]);
            tree.get(inputs[1]).add(inputs[0]);
        }

        dfs(1, tree, parent);
        StringBuilder sb = new StringBuilder();
        for (int i = 2; i <= n; i++) {
            sb.append(parent.get(i)).append("\n");
        }
        System.out.println(sb.toString());
    }

    static void dfs(Integer x, List<List<Integer>> tree, List<Integer> parent) {
        if (tree.get(x).isEmpty()) {
            return;
        }
        for (Integer con : tree.get(x)) {
            if (parent.get(con) == 0) {
                parent.set(con, x);
                dfs(con, tree, parent);
            }
        }
    }
}
