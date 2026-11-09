public class Solution {
    public static class CircuitBreaker {
        private final int failureThreshold;
        private final long openMs;
        private int failures;
        private boolean open;
        private long openedAt;
        private boolean trialInFlight;

        public CircuitBreaker(int failureThreshold, long openMs) {
            if (failureThreshold < 1) {
                throw new IllegalArgumentException("failureThreshold must be positive");
            }
            this.failureThreshold = failureThreshold;
            this.openMs = openMs;
        }

        private boolean halfOpen(long now) {
            return open && now - openedAt >= openMs;
        }

        public String state(long now) {
            if (!open) {
                return "CLOSED";
            }
            return halfOpen(now) ? "HALF_OPEN" : "OPEN";
        }

        public boolean allowRequest(long now) {
            if (!open) {
                return true;
            }
            if (!halfOpen(now)) {
                return false;
            }
            if (trialInFlight) {
                return false;
            }
            trialInFlight = true;
            return true;
        }

        public void recordSuccess() {
            failures = 0;
            open = false;
            trialInFlight = false;
        }

        public void recordFailure(long now) {
            if (open) {
                openedAt = now;
                trialInFlight = false;
                return;
            }
            failures++;
            if (failures >= failureThreshold) {
                open = true;
                openedAt = now;
                trialInFlight = false;
            }
        }
    }
}
