import java.util.*;
public class datascitest {
	static int num;
	static long total;
	public static void main(String args[]) {
		Scanner in = new Scanner(System.in);
		String string = in.next();

		for(String tag : string.split(",")) {

			total += Integer.parseInt(tag);
			num++;
		}

		System.out.println(num);
		System.out.println(total/num);
		in.close();
	}
}
