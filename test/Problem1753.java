package test;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Problem1753 {

	public static void main(String[] args) {

		//Scanner sc = new Scanner(System.in); // Scanner는 띄어쓰기 단위로 하나씩 읽어온다
		FastReader sc = new FastReader();

		int V = sc.nextInt(); // 바로 파일, 그순간 읽어오는데
		// br.readline() 미리 읽어와서 저장해준곳에서 꺼내온다. caching 느낌 lookadhead
		int E = sc.nextInt();
		int K = sc.nextInt();

		// Edge edge[V][V]
		ArrayList<Edge>[] edge = new ArrayList[V + 1];

		// java라서 new를 해줘야 한다.
		for (int i = 1; i <= V; i++) {
			edge[i] = new ArrayList<Edge>();
		}

		for (int i = 0; i < E; i++) {
			int u = sc.nextInt();
			int v = sc.nextInt();
			int w = sc.nextInt();
			edge[u].add(new Edge(v, w)); // v 다음 이동점, w는 가중치
		}

		boolean[] visit = new boolean[V + 1]; // 방문한 정점 표시 다익스트라에서는 정점을 딱 한번만 방문해요
		// visit대신 dist값이 -1인지 체크해도 되요
		int[] dist = new int[V + 1]; // 각정점에 도달하는데 걸린 cost

		// 초기화
		for (int i = 1; i <= V; i++) {
			dist[i] = -1;
		}

		// Priority Que를 만든다 poll 항상 최소값
		PriorityQueue<Point> que = new PriorityQueue<Point>();

		que.add(new Point(K, 0));

		while (!que.isEmpty()) {

			Point cur = que.poll();

			// System.out.println(cur.p + " : " + cur.w);

			if (visit[cur.p]) {
				continue;
			}

			visit[cur.p] = true;
			dist[cur.p] = cur.w; // 이게 최소값이 보장된다.
			// System.out.println(edge[cur.p]);
			for (Edge e : edge[cur.p]) {
				if (!visit[e.v]) {
					que.add(new Point(e.v, cur.w + e.w));
				}
			}

		}

		for (int i = 1; i <= V; i++) {
			if (dist[i] == -1)
				System.out.println("INF");
			else
				System.out.println(dist[i]);
		}

	}

	static class FastReader {
		BufferedReader br;
		StringTokenizer st;

		public FastReader() {
			br = new BufferedReader(new InputStreamReader(System.in));
		}

		String next() {
			while (st == null || !st.hasMoreElements()) {
				try {
					st = new StringTokenizer(br.readLine());
				} catch (IOException e) {
					e.printStackTrace();
				}
			}
			return st.nextToken();
		}

		int nextInt() {
			return Integer.parseInt(next());
		}
	}

	static class Point implements Comparable<Point> {

		int p;
		int w;

		Point(int p, int w) {
			this.p = p;
			this.w = w;
		}

		@Override
		public int compareTo(Point o) {
			return this.w - o.w;
		}

	}

	static class Edge {

		@Override
		public String toString() {
			return "Edge [v=" + v + ", w=" + w + "]";
		}

		int v;
		int w;

		// Scope
		Edge(int v, int w) {
			this.v = v; // this는 자기 instance this. 필드 멤버 (필드는 자바에서 class의 변수들)
			this.w = w;
		}

	}

}
