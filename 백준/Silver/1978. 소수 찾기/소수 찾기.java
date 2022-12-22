    import java.util.*;
    import java.io.*;
    public class Main {

    	public static void main(String[] args) throws IOException {
    	BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
    	BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
    	int num=Integer.parseInt(br.readLine());
    	int arr1[]=new int[num];
    	
    	int b=0;
    	
    	String arr2[]=br.readLine().split(" ");
    	for(int i=0;i<num;i++) {
    		arr1[i]=Integer.parseInt(arr2[i]);
    		int x=arr1[i]-1;
    		int a=0;
    		int aaa=x;
    		for(int j=0;j<aaa-1;j++) {
    			if(arr1[i]==1)
    				break;
    			
    			if(arr1[i]%x!=0) {
    				a++;
    			x--;
    		}
    		}
    		if(arr1[i]==a+2)
    			b++;
    	}
    	System.out.print(b);
}
    }