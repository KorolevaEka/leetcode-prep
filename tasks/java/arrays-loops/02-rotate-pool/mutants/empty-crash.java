public class Solution {
    public static int[] rotateRight(int[] items, int k) {
        int n = items.length;
        int[] result = new int[n];
        int shift = ((k % n) + n) % n;
        for (int i = 0; i < n; i++) {
            result[(i + shift) % n] = items[i];
        }
        return result;
    }
}
