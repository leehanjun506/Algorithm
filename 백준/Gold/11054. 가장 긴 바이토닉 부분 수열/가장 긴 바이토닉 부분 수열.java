import java.util.*;
public class Main {
	
	public static void main(String[] args) {
	Scanner scanner=new Scanner(System.in);
	int n=scanner.nextInt();
	int arr[]=new int[n];
	int dp1[]=new int[n];
	int dp2[]=new int[n];
	int dp3[]=new int[n];
	int max=1;
	for(int i=0;i<n;i++) {
		arr[i]=scanner.nextInt();
	}
	for(int i=0;i<n;i++) {
		dp1[i]=1;
		for(int j=0;j<n;j++) {
			if(arr[i]>arr[j])
				dp1[i]=Math.max(dp1[i], dp1[j]+1);
		}
	}

	for(int i=n-1;i>=0;i--) {
		dp2[i]=1;
		for(int j=n-1;j>i;j--) {
			if(arr[i]>arr[j])
			dp2[i]=Math.max(dp2[i], dp2[j]+1);
		}
	}
	/*for(int i=0;i<n;i++) {
		System.out.print(dp1[i]);
	}
	System.out.println();
	for(int i=0;i<n;i++) {
		System.out.print(dp2[i]);
	}	*/
	for(int i=0;i<n;i++) {
		dp3[i]=dp1[i]+dp2[i];
		max=Math.max(max, dp3[i]);
	}
	System.out.print(max-1);
}
	}
