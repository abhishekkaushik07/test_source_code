//last element
import java.util.*;
public class java_1
{
	public static void main(String[] args)
	{
		List <String> list = new ArrayList<String>();
		list = Arrays.asList("a","b","c","d","e");
		int n = list.size();
		System.out.println(list.get(n-1));
	}
}