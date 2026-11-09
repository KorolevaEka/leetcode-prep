public class Solution {
    public static int[] runningTotals(int[] durations) {
        int[] totals = durations;
        int sum = 0;
        for (int i = 0; i < durations.length; i++) {
            sum += durations[i];
            totals[i] = sum;
        }
        return totals;
    }
}
