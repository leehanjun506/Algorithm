    import java.util.*;
    import java.io.*;
    public class Main {

    	public static void main(String[] args) throws IOException {
    	BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
    	BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
    	int num=Integer.parseInt(br.readLine());
    	int arr[]=new int[11];
    	arr[0]=1;
    	arr[1]=2;
    	arr[2]=4;
    	for(int i=0;i<num;i++) {
    		int n=Integer.parseInt(br.readLine());
    		for(int j=3;j<n;j++) {
    			arr[j]=arr[j-1]+arr[j-2]+arr[j-3];
    		}
    		System.out.println(arr[n-1]);
    	}
}
    	}
    