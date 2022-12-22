import java.util.*;
public class Main {
	public static void main(String[] args) {
	Scanner scanner=new Scanner(System.in);
	int num=scanner.nextInt();
	Vector<Integer> v=new Vector<Integer>();
	for(int i=0;i<num;i++) {
		v.add(scanner.nextInt());
	}
	for(int i=0;i<num-1;i++) {
		if(v.get(i)==v.get(i+1))
			v.remove(i);
	}
	Object[] arr=v.toArray();
	Arrays.sort(arr);
	for(int i=0;i<num;i++) {
		System.out.println(arr[i]);
	}
}
}