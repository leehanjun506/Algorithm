    import java.util.*;
    import java.io.*;
    public class Main {

    	public static void main(String[] args) throws IOException {
    	BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
    	BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
    	int num=Integer.parseInt(br.readLine());
    	long arr[][]=new long[num][10];
    	for(int i=0;i<10;i++) {
    		arr[0][i]=1;
     	}
    	for(int j=1;j<num;j++) {
    		for(int k=0;k<10;k++) {
    			for(int l=0;l<=k;l++) {
    				arr[j][k]+=arr[j-1][l];
    				arr[j][k]%=10007;
    			}
    		}
    	}
    	long sum=0;
    	for(int q=0;q<10;q++) {
    		sum+=arr[num-1][q];
    		sum%=10007;
    	}
    	System.out.print(sum);
}
    	}
    