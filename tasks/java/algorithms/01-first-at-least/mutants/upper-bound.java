public class Solution {
    public static int firstAtLeast(int[] times, int target) {
        int lo = 0;
        int hi = times.length;
        while (lo < hi) {
            int mid = (lo + hi) >>> 1;
            if (times[mid] <= target) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        return lo;
    }
}
