public class Solution {
    public interface RetryPolicy {
        int maxAttempts();

        long delayBeforeRetryMs(int retryNumber);
    }

    private static void checkAttempts(int maxAttempts) {
        if (maxAttempts < 1) {
            throw new IllegalArgumentException("maxAttempts must be positive");
        }
    }

    private static void checkRetry(int maxAttempts, int retryNumber) {
        if (retryNumber < 1 || retryNumber > maxAttempts) {
            throw new IllegalArgumentException("no such retry: " + retryNumber);
        }
    }

    public static class FixedDelay implements RetryPolicy {
        private final int maxAttempts;
        private final long delayMs;

        public FixedDelay(int maxAttempts, long delayMs) {
            checkAttempts(maxAttempts);
            this.maxAttempts = maxAttempts;
            this.delayMs = delayMs;
        }

        public int maxAttempts() {
            return maxAttempts;
        }

        public long delayBeforeRetryMs(int retryNumber) {
            checkRetry(maxAttempts, retryNumber);
            return delayMs;
        }
    }

    public static class ExponentialBackoff implements RetryPolicy {
        private final int maxAttempts;
        private final long baseMs;
        private final long capMs;

        public ExponentialBackoff(int maxAttempts, long baseMs, long capMs) {
            checkAttempts(maxAttempts);
            this.maxAttempts = maxAttempts;
            this.baseMs = baseMs;
            this.capMs = capMs;
        }

        public int maxAttempts() {
            return maxAttempts;
        }

        public long delayBeforeRetryMs(int retryNumber) {
            checkRetry(maxAttempts, retryNumber);
            return Math.min(capMs, baseMs << (retryNumber - 1));
        }
    }

    public static long totalWaitMs(RetryPolicy policy) {
        long total = 0;
        for (int retry = 1; retry <= policy.maxAttempts() - 1; retry++) {
            total += policy.delayBeforeRetryMs(retry);
        }
        return total;
    }
}
