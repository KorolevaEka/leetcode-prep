import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class SolutionTest {
    @Test
    @DisplayName("фиксированная пауза")
    void fixed() {
        Solution.RetryPolicy policy = new Solution.FixedDelay(4, 250);
        assertEquals(4, policy.maxAttempts());
        assertEquals(250, policy.delayBeforeRetryMs(1));
        assertEquals(250, policy.delayBeforeRetryMs(3));
    }

    @Test
    @DisplayName("экспоненциальная пауза с потолком")
    void exponential() {
        Solution.RetryPolicy policy = new Solution.ExponentialBackoff(6, 100, 500);
        assertEquals(100, policy.delayBeforeRetryMs(1));
        assertEquals(200, policy.delayBeforeRetryMs(2));
        assertEquals(400, policy.delayBeforeRetryMs(3));
        assertEquals(500, policy.delayBeforeRetryMs(4));
        assertEquals(500, policy.delayBeforeRetryMs(5));
    }

    @Test
    @DisplayName("номер повтора вне диапазона")
    void retryOutOfRange() {
        Solution.RetryPolicy fixed = new Solution.FixedDelay(3, 10);
        assertThrows(IllegalArgumentException.class, () -> fixed.delayBeforeRetryMs(0));
        assertThrows(IllegalArgumentException.class, () -> fixed.delayBeforeRetryMs(3));
        Solution.RetryPolicy backoff = new Solution.ExponentialBackoff(3, 10, 1000);
        assertThrows(IllegalArgumentException.class, () -> backoff.delayBeforeRetryMs(0));
        assertThrows(IllegalArgumentException.class, () -> backoff.delayBeforeRetryMs(3));
        assertEquals(20, backoff.delayBeforeRetryMs(2));
    }

    @Test
    @DisplayName("maxAttempts меньше 1")
    void badAttempts() {
        assertThrows(IllegalArgumentException.class, () -> new Solution.FixedDelay(0, 10));
        assertThrows(IllegalArgumentException.class, () -> new Solution.ExponentialBackoff(0, 10, 100));
    }

    @Test
    @DisplayName("суммарное ожидание")
    void total() {
        assertEquals(750, Solution.totalWaitMs(new Solution.FixedDelay(4, 250)));
        assertEquals(1700, Solution.totalWaitMs(new Solution.ExponentialBackoff(6, 100, 500)));
        assertEquals(0, Solution.totalWaitMs(new Solution.FixedDelay(1, 999)));
        assertEquals(300, Solution.totalWaitMs(new Solution.ExponentialBackoff(3, 100, 10_000)));
    }

    @Test
    @DisplayName("totalWaitMs работает с любой политикой")
    void customPolicy() {
        Solution.RetryPolicy custom = new Solution.RetryPolicy() {
            public int maxAttempts() {
                return 4;
            }

            public long delayBeforeRetryMs(int retryNumber) {
                return retryNumber * 7L;
            }
        };
        assertEquals(7 + 14 + 21, Solution.totalWaitMs(custom));
    }
}
