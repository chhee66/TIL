package test;

import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.Scanner;

public class Problem1753 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in); //Scanner는 띄어쓰기 단위로 하나씩 읽어온다
		  
		System.out.println("!");
		int V = sc.nextInt();
		int E = sc.nextInt();
		int K = sc.nextInt();
		System.out.println("!");
		//Edge edge[V][V]
		ArrayList<Edge>[] edge = new ArrayList[V + 1];

		// java라서 new를 해줘야 한다.
		for (int i = 1; i <= V; i++) {
			edge[i] = new ArrayList<Edge>();
		}

		for (int i = 0; i < E; i++) {
			int u = sc.nextInt();
			int v = sc.nextInt();
			int w = sc.nextInt();
			edge[u].add(new Edge(v, w)); //v 다음 이동점, w는 가중치
		}

		
		boolean[] visit = new boolean[V + 1]; //방문한 정점 표시 다익스트라에서는 정점을  딱 한번만 방문해요
		//visit대신 dist값이 -1인지 체크해도 되요
		int[] dist = new int[V + 1];     // 각정점에 도달하는데 걸린 cost

		
		//초기화
		for (int i = 1; i <= V; i++) {
			dist[i] = -1;
		}

		//Priority Que를 만든다 poll 항상 최소값
		PriorityQueue<Point> que = new PriorityQueue<Point>();

		que.add(new Point(K, 0));

		while (!que.isEmpty()) {

			Point cur = que.poll();
			
			//System.out.println(cur.p + " : " + cur.w);

			if (visit[cur.p]) {
				continue;
			}
			
			visit[cur.p] = true;
			dist[cur.p] = cur.w; // 이게 최소값이 보장된다.
			//System.out.println(edge[cur.p]);
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
