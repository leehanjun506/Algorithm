import java.util.*;
public class Main {
	static int visit[]=new int[300001];
	static void dfs(int a,int p) {
		int sum=0;
		visit[a]++;
		if(visit[a]==3)
			return;
		while(a!=0) {
			sum+=Math.pow((a%10), p);
			a/=10;
		}
		dfs(sum,p);
	}
	
	public static void main(String[] args) {
	Scanner scanner=new Scanner(System.in);
	int a=scanner.nextInt();
	int p=scanner.nextInt();
	int x=0;
	dfs(a,p);
	for(int i=0;i<visit.length;i++) {
		if(visit[i]==1)
			x++;
	}
	System.out.print(x);
}
	}
