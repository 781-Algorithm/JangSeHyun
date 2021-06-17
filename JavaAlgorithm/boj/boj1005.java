package boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class boj1005 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int t = Integer.parseInt(br.readLine());
        while (t != 0) {
            st = new StringTokenizer(br.readLine(), " ");
            t -= 1;
            int n = Integer.parseInt(st.nextToken());
            int k = Integer.parseInt(st.nextToken());
            int[] delay = new int[n + 1];

            st = new StringTokenizer(br.readLine(), " ");
            for (int i = 1; i < n + 1; i++) {
                delay[i] = Integer.parseInt(st.nextToken());
            }

            ArrayList<Integer>[] graph = new ArrayList[n + 1];
            for (int i = 1; i <= n; i++) {
                graph[i] = new ArrayList<>();
            }
            int[] inDegree = new int[n + 1];
            for (int i = 0; i < k; i++) {
                st = new StringTokenizer(br.readLine(), " ");
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                graph[a].add(b);
                inDegree[b] += 1;
            }
            int w = Integer.parseInt(br.readLine());
            topologySort(n, w, graph, inDegree, delay);
        }
    }

    static void topologySort(int n, int w, ArrayList<Integer>[] graph, int[] inDegree, int[] delay) {
        Deque<Integer[]> q = new ArrayDeque<>();
        int[] times = new int[n + 1];

        for (int i = 1; i < n + 1; i++) {
            if (inDegree[i] == 0) {
                q.add(new Integer[]{i, delay[i]});
                times[i] = delay[i];
            }
        }
        while (!q.isEmpty()) {
            Integer[] info = q.pollFirst();

            for (Integer next : graph[info[0]]) {
                inDegree[next] -= 1;
                times[next] = Math.max(times[next], info[1] + delay[next]);
                if (inDegree[next] == 0) {
                    q.addLast(new Integer[]{next, times[next]});
                }
            }
        }
        System.out.println(times[w]);
    }

}
