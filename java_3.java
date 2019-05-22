//kth element
import java.util.*;
public class java_3
{
	public static void main(String[] args)
	{
		List <String> list = new ArrayList<String>();
		list = Arrays.asList("a","b","c","d","e");
		Scanner input = new Scanner(System.in);
		int k =input.nextInt();
		System.out.println(list.get(k-1));
	}
}