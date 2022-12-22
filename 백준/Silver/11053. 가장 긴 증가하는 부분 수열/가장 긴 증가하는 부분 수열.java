import java.util.*;
public class Main {
	
	public static void main(String[] args) {
	Scanner scanner=new Scanner(System.in);
	int n=scanner.nextInt();
	int arr[]=new int[n];
	int dp[]=new int[n];

	for(int i=0;i<n;i++) {
		arr[i]=scanner.nextInt();
	}
	for(int i=0;i<n;i++) {
		dp[i]=1;
		for(int j=0;j<i;j++) {
			if(arr[i]>arr[j])
				dp[i]=Math.max(dp[i], dp[j]+1);
			}
		}
	for(int i=1;i<n;i++) {
		dp[i]=Math.max(dp[i], dp[i-1]);
	}
	System.out.print(dp[n-1]);
	}
	
}
