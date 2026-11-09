public class Solution {
    public interface RetryPolicy {
        int maxAttempts();

        long delayBeforeRetryMs(int retryNumber);
    }

    public static class FixedDelay implements RetryPolicy {
        public FixedDelay(int maxAttempts, long delayMs) {
            throw new UnsupportedOperationException("TODO");
        }

        public int maxAttempts() {
            throw new UnsupportedOperationException("TODO");
        }

        public long delayBeforeRetryMs(int retryNumber) {
            throw new UnsupportedOperationException("TODO");
        }
    }

    public static class ExponentialBackoff implements RetryPolicy {
        public ExponentialBackoff(int maxAttempts, long baseMs, long capMs) {
            throw new UnsupportedOperationException("TODO");
        }

        public int maxAttempts() {
            throw new UnsupportedOperationException("TODO");
        }

        public long delayBeforeRetryMs(int retryNumber) {
            throw new UnsupportedOperationException("TODO");
        }
    }

    public static long totalWaitMs(RetryPolicy policy) {
        throw new UnsupportedOperationException("TODO");
    }
}
