import java.io.*;
import java.util.*;

class TrieNode {
	private char value;
	private HashMap<Character, TrieNode> children;
	private boolean IsEnd;
	private int count;

	public TrieNode(char value) {
		this.value = value;
		this.children = new HashMap<>();
	
		IsEnd = false;
		this.count = 1;
	}

	public char getValue() {
		return value;
	}

	public void setIsEnd(boolean val) {
		IsEnd = val;
	}

	public void setCount(int value) {
		this.count = value;
	}

	public int getCount() {
		return this.count;
	}

	public boolean isEnd() {
		return IsEnd;
	}

	public HashMap<Character, TrieNode> getChildren() {
		return this.children;
	}

}

class Trie {
	TrieNode root;

	public Trie() {
		root = new TrieNode((char) 0);
	}

	public void insert(String word) {
		int len = word.length();
		TrieNode crawl = root;

		for (int level = 0; level < len; level++) {
			HashMap<Character, TrieNode> temp = crawl.getChildren();
			char ch = word.charAt(level);
			if (temp.containsKey(ch)) {
				crawl = temp.get(ch);
				TrieNode nod = crawl;
				int val = nod.getCount();
				nod.setCount(val + 1);
				temp.put(ch, nod);
			} 
			else {
				TrieNode temps = new TrieNode(ch);
				temp.put(ch, temps);
				crawl = temps;
			}
		}
		crawl.setIsEnd(true);
	}

	public int findCount(String word) {
		int len = word.length();
		TrieNode crawl = root;
		int result = 0;

		for (int level = 0; level < len; level++) {
			char ch = word.charAt(level);
			HashMap<Character, TrieNode> temp = crawl.getChildren();
			if (temp.containsKey(ch)) {
				crawl = temp.get(ch);
				result = crawl.getCount();
				
			} else {
                result =0;
				break;

			}
		}
		return result;
	}
}

public class Trieimple {
    public static void main(String[] args) {
            System.out.println("Enter number of test cases: ");
            Scanner in = new Scanner(System.in);
            int n = in.nextInt();
            Trie tr=new Trie();

            for (int a0 = 0; a0 < n; a0++) {
            	   System.out.println("opcode: ");
            	   System.out.println("'1' for  add to phonebook ");
            	   System.out.println("'2' for find the number of contacts with given prefix ");
                String op = in.next();
                String contact = in.next();
                if (op.equals("add")) {
                    tr.insert(contact);
                }
                else if(op.equals("find")){
                    int value=tr.findCount(contact);
                    System.out.println(value+"");
                }
            }
        }
}
