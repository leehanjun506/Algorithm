import java.util.*;
public class Main {
public static void main(String []args){
    Scanner sc=new Scanner(System.in);
    int num=sc.nextInt();
    int arr[]=new int[num];
    int data;
    for(int i=0;i<num;i++) {
    	int a=sc.nextInt();
    	int b=sc.nextInt();
    	data=a%10;
        if(data==0) {
    			arr[i]=10;
                continue;
    		}
    	for(int j=1;j<b;j++) {
    		data=data*a%10;
    	}
    	arr[i]=data%10;
    }
    for(int i=0;i<num;i++) {
    	System.out.println(arr[i]);
    }
      
}
}