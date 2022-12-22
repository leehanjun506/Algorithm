import java.util.*;
public class Main {
	public static void main(String[] args) {
	Scanner scanner=new Scanner(System.in);
	int maxinstall=1;
	int n=scanner.nextInt();
	int dp[]=new int[n];
	int arr[][]=new int[n][2];
	for(int i=0;i<n;i++) {
		for(int j=0;j<2;j++) {
			arr[i][j]=scanner.nextInt();
		}
	}
	Arrays.sort(arr,Comparator.comparingInt(o1->o1[0]));
	for(int i=0;i<n;i++) {
		dp[i]=1;
		for(int j=0;j<i;j++) {
			if(arr[j][1]<arr[i][1]) {
				dp[i]=Math.max(dp[i],dp[j]+1);
			}
		}
		maxinstall=Math.max(maxinstall, dp[i]);
	}
	System.out.print(n-maxinstall);
	}
}