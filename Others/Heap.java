import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
class Heaps{
    int capacity=100000;
    int size=0; // number of elements in our heap (index is size-1)
    int [] items=new int [capacity];
    int heaptype=0;// 0 for minheap 1 for maxheap
    Heaps(int type){
        this.heaptype=type;
    }
    
    private int getLeftIndex(int parentIndex){ return 2* parentIndex+1;}
    private int getRightIndex(int parentIndex){ return 2* parentIndex+2;}
    private int getParentIndex(int index){ return (index-1)/2;}
    
    private boolean hasLeft(int index){ return getLeftIndex(index)<size ;}
    private boolean hasRight(int index){ return getRightIndex(index)<size ;}
    private boolean hasParent(int index){ return getParentIndex(index)>=0 ;}
    
    private int leftChild(int index){ return items[getLeftIndex(index)];}
    private int rightChild(int index){ return items[getRightIndex(index)];}
    private int parent(int index){ return items[getParentIndex(index)];}
    
    public int getSize(){ return this.size;   }
    private void swap(int ind1, int ind2){
        int temp;
        temp=items[ind1];
        items[ind1]=items[ind2];
        items[ind2]=temp;
    }
    private void ensureExtraCapacity(){
        if(size==capacity){
            items=Arrays.copyOf(items,capacity*2);
            capacity *= 2;
        }
    }
    public int peek(){
        if(size==0) throw new IllegalStateException();
        return items[0];
    }
    public int poll(){
        if(size==0) throw new IllegalStateException();
        int item=items[0];
        items[0]=items[size-1];
        size--;
        heapifyDown();
        return item;
    }
    public void add(int item){
        ensureExtraCapacity();
        System.out.print("element is "+item);
        items[size] = item;
        size++;
        heapifyUp();        
    }
    public void heapifyUp(){
        int index= size-1;
        if(this.heaptype==0){
            System.out.println("  its min heap added element" +this.getSize());
            while(hasParent(index) && parent(index) >items[index]){
                swap(getParentIndex(index),index);
                index=getParentIndex(index);
            }
        }
        else{
            System.out.println("  its max heap added element "+this.getSize());
            while(hasParent(index) && parent(index)<items[index]){
                swap(getParentIndex(index),index);
                index=getParentIndex(index);
            }           
        }
    }
    public void heapifyDown(){
        int index=0;
        if(this.heaptype==0){
            System.out.println("its min heap deleted element");
            while(hasLeft(index)){
                int minimum=getLeftIndex(index);
                if(hasRight(index) && rightChild(index)<leftChild(index)){
                    minimum= getRightIndex(index);
                }
                if(items[index]<items[minimum]){
                    break;
                }
                else{
                    swap(index,minimum);
                }
                index=minimum;
            }
        }
        else{
            System.out.println("its max heap deleted element");
            while(hasLeft(index)){
                int maximum=getLeftIndex(index);
                if(hasRight(index) && rightChild(index) >leftChild(index)){
                    maximum=getRightIndex(index);
                }
                if(items[index]>items[maximum]){
                    break;
                }
                else{
                    swap(index,maximum);
                }
                index=maximum;
            }
            
        }
    }
}
public class Solution2 {
    public static double printMedian(Heaps minheap,Heaps maxheap){
        double med=0;
        int median;
        if(minheap.getSize()-maxheap.getSize() >1) {
        	maxheap.add(minheap.poll());
        }else if(maxheap.getSize()-minheap.getSize() >1){
        	minheap.add( maxheap.poll());	
        }
        if(minheap.getSize() == maxheap.getSize()){
            med=(minheap.peek()+ maxheap.peek())/2.0;
           System.out.printf("%.1f\n", med);
            
        }
        else if(minheap.getSize() > maxheap.getSize()){
            
            System.out.println("in here");
            median=minheap.peek();  
            med=(double)median;
            
            System.out.println(median + ".0");
        }
        else{
            
            median=maxheap.peek();
            med=(double)median;
            System.out.println(median + ".0");
        }
            
       // System.out.println(median+"");
        //System.out.printf("%.1f", median);
        System.out.println("median is  "+med);
        return med;
    }
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        
        int[] arr = new int[n];
        // creating 2 heaps min and max heap
        Heaps minheap = new Heaps(0);
        Heaps maxheap = new Heaps(1);
        double median=0;
        for(int a_i=0; a_i < n; a_i++){
            arr[a_i] = in.nextInt();
            if(a_i < 2 ){
                if(a_i==0){
                    
                    median=(double)arr[0];
                    System.out.println(median);
                    continue;
                }
                if(arr[0]>arr[1]){
                    minheap.add(arr[0]);
                    maxheap.add(arr[1]);  
                    
                }else{
                    minheap.add(arr[1]);
                    maxheap.add(arr[0]);
                }
                median=printMedian(minheap,maxheap);
                System.out.println("its median   "+median);
                continue;            
            }
            if(arr[a_i] > median){
                minheap.add(arr[a_i]);
            }else{
                maxheap.add(arr[a_i]);
            }          
            median=printMedian(minheap,maxheap);
        }
        
        
    }
}
