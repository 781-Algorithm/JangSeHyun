package boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static List<HashMap<Integer, Integer>> tree = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int v = Integer.parseInt(br.readLine());
        int[] distance = new int[v + 1];

        for (int i = 0; i <= v; i++) {
            tree.add(new HashMap<>());
            distance[i] = -1;
        }

        for (int i = 0; i < v; i++) {
            int[] inputs = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            HashMap<Integer, Integer> temp = tree.get(inputs[0]);
            for (int j = 1; j < inputs.length-1; j += 2) {
                temp.put(inputs[j], inputs[j + 1]);
            }
        }

        distance[1] = 0;
        dfs(1, 0, distance);
        int max_idx = 0;
        int max_val = 0;
        for (int i = 0; i < distance.length; i++) {
            if (distance[i] > max_val) {
                max_idx = i;
                max_val = distance[i];
            }
            distance[i] = -1;
        }
        distance[max_idx] = 0;
        dfs(max_idx,0,distance);
        System.out.println(Arrays.stream(distance).max().getAsInt());
    }

    static void dfs(Integer x, Integer cost, int[] distance) {

        tree.get(x).forEach((k,v)->{
            if (distance[k] == -1) {
                distance[k] = cost + v;
                dfs(k, cost + v, distance);
            }
        });
    }
}
