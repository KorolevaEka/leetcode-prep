public class Solution {
    public static int[] runningTotals(int[] durations) {
        int[] totals = new int[durations.length];
        int sum = 0;
        for (int i = 0; i < durations.length; i++) {
            totals[i] = sum;
            sum += durations[i];
        }
        return totals;
    }
}
