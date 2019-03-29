public class Main {
	public static void main(String[] args) {
		FindFile findFile = new FindFile();
		String[] found = findFile.foundFile(args);
		for(int i = 0; i < found.length; i++) {
			String s = found[i];
			if(s != null)
				System.out.println(s);
		}
	}
}