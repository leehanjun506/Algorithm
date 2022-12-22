    import java.util.*;
    import java.io.*;
    public class Main {

    	public static void main(String[] args) throws IOException {
    	BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
    	BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
    	int num=Integer.parseInt(br.readLine());
    	long arr[][]=new long[num][10];
    	for(int i=1;i<10;i++) {
    		arr[0][i]=1;
    	}
    	for(int j=1;j<num;j++) {
    		for(int k=0;k<10;k++) {
    			if(k==0)
    				arr[j][k]=arr[j-1][k+1]%1000000000;
    			else if(k==9)
    				arr[j][k]=arr[j-1][k-1]%1000000000;
    			else
    			arr[j][k]=arr[j-1][k-1]+arr[j-1][k+1]%1000000000;
    		}
    	}
    	long sum=0;
    	for(int k=0;k<10;k++) {
    		sum+=arr[num-1][k];
    	}
    	System.out.print(sum%1000000000);
}
    	}
    