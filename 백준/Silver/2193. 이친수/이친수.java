    import java.util.*;
    import java.io.*;
    public class Main {

    	public static void main(String[] args) throws IOException {
    	BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
    	BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
    	int num=Integer.parseInt(br.readLine());
    	long dp[][]=new long[num][2];
    	dp[0][0]=0;
    	dp[0][1]=1;
    	for(int i=1;i<num;i++) {
    		for(int j=0;j<2;j++) {
    			if(j==1)
    				dp[i][j-1]+=dp[i-1][j];
    			else {
    			dp[i][j]=dp[i-1][j];
    			dp[i][j+1]=dp[i-1][j];
    		}
    			}
    	}
    	System.out.print(dp[num-1][0]+dp[num-1][1]);
    	}
    }    