import java.io.*;
public class Main {
public static void main(String [] args)  throws IOException {
	BufferedReader bf=new BufferedReader(new InputStreamReader(System.in));
	int dp[][]=new int[41][2];
	String s=bf.readLine();
	int testcase= Integer.parseInt(s);
	dp[0][0]=1;
	dp[0][1]=0;
	dp[1][0]=0;
	dp[1][1]=1;
	for(int i=0;i<testcase;i++) {
	int x=Integer.parseInt(bf.readLine());
		for(int n=2;n<=x;n++) {
			dp[n][0]=dp[n-1][0]+dp[n-2][0];
			dp[n][1]=dp[n-1][1]+dp[n-2][1];
		}
		System.out.println(dp[x][0]+" "+dp[x][1]);
	}

	
}
}