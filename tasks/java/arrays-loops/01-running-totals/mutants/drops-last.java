public class Solution {
    public static int[] runningTotals(int[] durations) {
        int[] totals = new int[durations.length];
        int sum = 0;
        for (int i = 0; i < durations.length - 1; i++) {
            sum += durations[i];
            totals[i] = sum;
        }
        return totals;
    }
}
