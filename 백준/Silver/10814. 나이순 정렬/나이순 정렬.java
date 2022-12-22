import java.util.*;

public class Main {

	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int num=sc.nextInt();
		ArrayList<List> a= new ArrayList<>();
		for(int i=0;i<num;i++) {
			a.add(new List(sc.nextInt(),sc.next(),i));
		}
		Collections.sort(a,new Comparator<List>() {
			public int compare(List a,List b) {
				return a.number-b.number;
			}
		});
		Collections.sort(a,new Comparator<List>() {
			public int compare(List a,List b) {
				return a.age-b.age;
			}
		});
		for(int i=0;i<num;i++) {
			System.out.println(a.get(i).age+" "+a.get(i).name);
		}
		}
}
 class List{
	int age;
	String name;
	int number;
	List(int age,String name,int number){
		this.age=age;
		this.name=name;
		this.number=number;
	}
}	

