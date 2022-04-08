public class CallByReference8 {

    public void swap(int x, int y) {
        int t = x;
        x = y;
        y = t;
        System.out.println("Inside swap(): " + x + " " + y);
    }

    public static void main(String[] args) {
        CallByReference8 obj = new CallByReference8();
        int x = 10, y = 20;

        System.out.println("Before swap(): " + x + " " + y);
        obj.swap(x, y);
        System.out.println("After swap(): " + x + " " + y);
    }
}