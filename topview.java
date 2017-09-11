import java.util.*;
 
// Class for a tree node
//reference
// GFG- http://www.geeksforgeeks.org/print-nodes-top-view-binary-tree/
class Node
{
    // Members
    int data;
    Node left, right;
 
    // Constructor
    public Node(int key)
    {
        this.data = key;
        left = right = null;
    }
}
 
// A class to represent a queue item. The queue is used to do Level
// order traversal. Every Queue item contains node and horizontal
// distance of node from root
class QItem
{
   Node node;
   int hd;
   public QItem(Node n, int h)
   {
        node = n;
        hd = h;
   }
}
class Tree{
	Node  root;
	public Tree(){
		root=null;
	}
	public Tree(Node root) {
		super();
		this.root = root;
	}
	public void printTopView(){
		//base case
		if(root==null){ return ;	}
		HashSet<Integer> set =new HashSet<>();
		
		Queue<QItem> que= new LinkedList<QItem>();
		que.add(new QItem(root,0 ));
		while(!que.isEmpty()){
			QItem qi = que.remove();
			int hd=qi.hd;
			Node n= qi.node;
			if(!set.contains(hd)){
				set.add(hd);
				System.out.print(n.data+" ");
			}
			if(n.left !=null){
				que.add(new QItem(n.left,hd-1));
			}
			if(n.right!=null){
				que.add(new QItem(n.right,hd+1));

			}
			
		}
	
	}
}
public  class topview {

	 public static void main(String[] args)
	    {
	        /* Create following Binary Tree
	             1
	           /  \
	          2    3
	           \
	            4
	             \
	              5
	               \
	                6*/
	        Node root = new Node(1);
	        root.left = new Node(2);
	        root.right = new Node(3);
	        root.left.right = new Node(4);
	        root.left.right.right = new Node(5);
	        root.left.right.right.right = new Node(6);
	        Tree t = new Tree(root);
	        System.out.println("Following are nodes in top view of Binary Tree");
	        t.printTopView();
	    }


}
