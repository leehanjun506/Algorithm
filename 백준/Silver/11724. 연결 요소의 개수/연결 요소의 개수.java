import java.util.Scanner;
public class Main {
	static int visit[];
	static int arr[][];
	static void DFS(int start) {
		
		visit[start-1]=1;
		for(int i=0;i<visit.length;i++) {
				if(visit[i]==0&&arr[start-1][i]==1) {
					DFS(i+1);
			}
		}
	return;
}


public static void main(String [] args)  {
	Scanner sc=new Scanner(System.in);
	int n=sc.nextInt();
	int e=sc.nextInt();
	int num=0;
	arr=new int[n][n];
	visit=new int[n];
	for(int i=0;i<e;i++) {
		int a1=sc.nextInt();
		int a2=sc.nextInt();
		arr[a1-1][a2-1]=1;
		arr[a2-1][a1-1]=1;
		}
	for(int i=0;i<n;i++) {
			if(visit[i]==0) {
				DFS(i+1);
				num++;
			}
		}
	System.out.print(num);
	}
}
