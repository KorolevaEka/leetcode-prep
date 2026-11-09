import java.util.Arrays;

public class Solution {
    public static int maxParallel(int[][] runs) {
        int n = runs.length;
        int[] starts = new int[n];
        int[] ends = new int[n];
        for (int i = 0; i < n; i++) {
            starts[i] = runs[i][0];
            ends[i] = runs[i][1];
        }
        Arrays.sort(starts);
        Arrays.sort(ends);
        int current = 0;
        int best = 0;
        int j = 0;
        for (int i = 0; i < n; i++) {
            while (ends[j] <= starts[i]) {
                current--;
                j++;
            }
            best = Math.max(best, current);
            current++;
        }
        return best;
    }
}
