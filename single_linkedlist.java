
class single_linkedlist {
    
    public static void main(String[] args) {
       
    }
}

class Node {
        Node next = null;
        int data;

        public Node(int data) {
            this.data = data;
        }

        void appendToTail(int data) {
            Node end = new Node(data);
            Node n = this;
            while (n.next != null ) {
                n = n.next;     // ?
            }
            n.next = end; // ??? 
        }

}