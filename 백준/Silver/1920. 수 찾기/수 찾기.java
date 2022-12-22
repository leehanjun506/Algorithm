import java.util.Scanner;
import java.util.Arrays;
public class Main {
	static int binary(int[]arr1,int arr2,int n,int m) {
		int left=0;
		int right=n-1;
		int mid;
		int flag=0;
		while(right>=left) {
			mid=(left+right)/2;
			if(arr2==arr1[mid]) {
				flag=1;
				break;
			}
			if(arr2<arr1[mid]) {
				right=mid-1;
			}
			else {
				left=mid+1;
			}
		}
		return flag;
	}
public static void main(String []args){
    Scanner sc=new Scanner(System.in);
    int n=sc.nextInt();
    int[] arr1=new int[n];
    for(int i=0;i<arr1.length;i++) {
    	arr1[i]=sc.nextInt();
    }
    Arrays.sort(arr1);
    int m=sc.nextInt();
    int[] arr2=new int[m];
    for(int i=0;i<arr2.length;i++) {
    	arr2[i]=sc.nextInt();
    }
    for(int i=0;i<arr2.length;i++) {
    	System.out.println(binary(arr1,arr2[i],n,m));
    }
    
}
}