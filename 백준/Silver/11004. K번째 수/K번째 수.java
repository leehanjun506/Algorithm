import java.util.*;
import java.io.*;
public class Main {
	static class Card{
		long num;
		long sum;
		public Card(long num,long sum) {
			this.num=num;
			this.sum=sum;
		}
	}
	
	public static void main(String[] args) throws IOException {
	BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
	BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
	String s1[]=br.readLine().split(" ");
	ArrayList<Integer> list=new ArrayList<>();
	String s2[]=br.readLine().split(" ");
	for(int i=0;i<Integer.parseInt(s1[0]);i++) {
		list.add(Integer.parseInt(s2[i]));
	}
	Collections.sort(list);
	bw.write(list.get(Integer.parseInt(s1[1])-1).toString());
	bw.flush();
	
}
}

