public class CallByReference7 {

    public void swap(int[] arr, int x, int y) {
        int t = arr[x];
        arr[x] = arr[y];
        arr[y] = t;
        System.out.println("Inside swap(): " + arr[x] + " " + arr[y]);
    }

    public static void main(String[] args) {
        CallByReference7 obj = new CallByReference7();
        int[] arr = {10, 20};
        int x = 0, y = 1;

        System.out.println("Before swap(): " + arr[x] + " " + arr[y]);
        obj.swap(arr, x, y);
        System.out.println("After swap(): " + arr[x] + " " + arr[y]);
    }
}