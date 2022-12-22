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
	int tc=sc.nextInt();
	for(int k=0;k<tc;k++) {
		int n=sc.nextInt();
		int num=0;
		arr=new int[n][n];
		visit=new int[n];
	for(int i=0;i<n;i++) {
		int a1=sc.nextInt();
		arr[i][a1-1]=1;
		}
	for(int i=0;i<n;i++) {
			if(visit[i]==0) {
				DFS(i+1);
				num++;
			}
		}
	System.out.println(num);
	for(int i=0;i<n;i++) {
		visit[i]=0;
	}
		}
	}
}
