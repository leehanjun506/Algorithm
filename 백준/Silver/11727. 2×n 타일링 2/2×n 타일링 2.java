    import java.util.*;
    import java.io.*;
    public class Main {

    	public static void main(String[] args) throws IOException {
    	BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
    	BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
    	int num=Integer.parseInt(br.readLine());
    	int arr[]=new int[num+1];
    	arr[0]=1;
    	arr[1]=3;
    	for(int i=2;i<num;i++) {
    		arr[i]=arr[i-1]+2*arr[i-2];
    		arr[i]%=10007;
    	}
    	System.out.print(arr[num-1]);
}
    	}
    