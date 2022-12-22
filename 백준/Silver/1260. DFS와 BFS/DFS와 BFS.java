import java.util.*;
public class Main {
	static int arr[][];
	static int check[];
	static int check2[];
	static Queue<Integer> queue=new LinkedList<>();
	static Queue<Integer> visit=new LinkedList<>();
	public static void main(String[] args) {
	Scanner scanner=new Scanner(System.in);
	int v=scanner.nextInt();
	int e=scanner.nextInt();
	int first=scanner.nextInt();
	int new_first=first;
	arr=new int[v][v];
	check=new int[v];
	check2=new int[v];
	int a1;
	int a2;
	for(int i=0;i<e;i++) {
		a1=scanner.nextInt();
		a2=scanner.nextInt();
		arr[a1-1][a2-1]=1;
		arr[a2-1][a1-1]=1;
		}
	
	dfs(first);
	System.out.println();
	for(int i=0;i<v;i++) {
		check[i]=0;
	}
	bfs(new_first,v);
	int size=visit.size();
	for(int i=0;i<size;i++) {
		System.out.print(visit.poll()+" ");
	}
	}
	
	static void dfs(int first) {
		System.out.print(first+" ");
		check[first-1]=1;
		for(int i=0;i<check.length;i++) {
			if(check[i]==0&&arr[first-1][i]==1) {
				dfs(i+1);
			}
		}
	}
	
	static void bfs(int first,int v) {
		visit.add(first);
		check[first-1]=1;
		while(true) {
			for(int i=0;i<v;i++) {
				if(arr[first-1][i]==1&&check[i]==0&&check2[i]==0) {
					queue.add(i+1);
					check2[i]=1;
				}
			}
			if(queue.isEmpty()==true)
				break;
			first=queue.peek();
			check[first-1]=1;
			visit.add(queue.poll());
			
			
		}

	}
}

