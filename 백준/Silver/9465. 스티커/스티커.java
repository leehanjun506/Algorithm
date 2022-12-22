    import java.util.*;
    import java.io.*;
    public class Main {

    	public static void main(String[] args) throws IOException {
    	BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
    	BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
    	int tc=Integer.parseInt(br.readLine());
    	for(int i=0;i<tc;i++) {
    		int num=Integer.parseInt(br.readLine());
    		int arr[][]=new int[2][num];
    		int dp[][]=new int [2][num];
    		String arr1[]=br.readLine().split(" ");
    		String arr2[]=br.readLine().split(" ");
    		for(int j=0;j<num;j++) {
    			arr[0][j]=Integer.parseInt(arr1[j]);
    			arr[1][j]=Integer.parseInt(arr2[j]);
    		}
    		for(int k=0;k<num;k++) {
    			if(k==0) {
    				dp[0][k]=arr[0][k];
    				dp[1][k]=arr[1][k];
    			}
    			else if(k==1) {
    				dp[0][k]=arr[0][k]+arr[1][k-1];
    				dp[1][k]=arr[1][k]+arr[0][k-1];
    				}
    			else {
    			dp[0][k]=Math.max(dp[1][k-1],dp[1][k-2])+arr[0][k];
    			dp[1][k]=Math.max(dp[0][k-1], dp[0][k-2])+arr[1][k];
    			}
    		}
    		System.out.println(Math.max(dp[0][num-1], dp[1][num-1]));
    		}
    	}
    }    