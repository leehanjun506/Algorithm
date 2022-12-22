import java.util.*;
public class Main {
	
	public static void main(String[] args) {
	Scanner scanner=new Scanner(System.in);
	int n=scanner.nextInt();
	int arr[]=new int[n];
	int dp[]=new int[n];
	int max=0;
	for(int i=0;i<n;i++) {
		arr[i]=scanner.nextInt();
	}
	for(int i=0;i<n;i++) {
		dp[i]=arr[i];
		for(int j=0;j<i;j++) {
			if(arr[i]>arr[j])
				dp[i]=Math.max(arr[i]+dp[j], dp[i]);
			
		}
		max=Math.max(dp[i], max);
	}
	System.out.print(max);

	}
	
}
