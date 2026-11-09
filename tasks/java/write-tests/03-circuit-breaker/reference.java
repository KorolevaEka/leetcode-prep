import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class SolutionTest {
    @Test
    void invalidThreshold() {
        assertThrows(IllegalArgumentException.class, () -> new Solution.CircuitBreaker(0, 1000));
    }

    @Test
    void startsClosed() {
        Solution.CircuitBreaker cb = new Solution.CircuitBreaker(3, 1000);
        assertEquals("CLOSED", cb.state(0));
        assertTrue(cb.allowRequest(0));
    }

    @Test
    void opensExactlyAtThreshold() {
        Solution.CircuitBreaker cb = new Solution.CircuitBreaker(3, 1000);
        cb.recordFailure(10);
        cb.recordFailure(20);
        assertEquals("CLOSED", cb.state(20));
        assertTrue(cb.allowRequest(20));
        cb.recordFailure(30);
        assertEquals("OPEN", cb.state(30));
        assertFalse(cb.allowRequest(30));
    }

    @Test
    void successResetsFailureCount() {
        Solution.CircuitBreaker cb = new Solution.CircuitBreaker(3, 1000);
        cb.recordFailure(1);
        cb.recordFailure(2);
        cb.recordSuccess();
        cb.recordFailure(3);
        cb.recordFailure(4);
        assertEquals("CLOSED", cb.state(4));
        cb.recordFailure(5);
        assertEquals("OPEN", cb.state(5));
    }

    @Test
    void becomesHalfOpenExactlyAfterOpenMs() {
        Solution.CircuitBreaker cb = new Solution.CircuitBreaker(1, 1000);
        cb.recordFailure(100);
        assertEquals("OPEN", cb.state(1099));
        assertFalse(cb.allowRequest(1099));
        assertEquals("HALF_OPEN", cb.state(1100));
    }

    @Test
    void halfOpenAllowsSingleTrial() {
        Solution.CircuitBreaker cb = new Solution.CircuitBreaker(1, 1000);
        cb.recordFailure(0);
        assertTrue(cb.allowRequest(1000));
        assertFalse(cb.allowRequest(1000));
        assertFalse(cb.allowRequest(5000));
        assertEquals("HALF_OPEN", cb.state(5000));
    }

    @Test
    void trialSuccessClosesAndCounterRestarts() {
        Solution.CircuitBreaker cb = new Solution.CircuitBreaker(2, 1000);
        cb.recordFailure(0);
        cb.recordFailure(1);
        assertTrue(cb.allowRequest(1001));
        cb.recordSuccess();
        assertEquals("CLOSED", cb.state(1001));
        assertTrue(cb.allowRequest(1001));
        assertTrue(cb.allowRequest(1001));
        cb.recordFailure(1002);
        assertEquals("CLOSED", cb.state(1002));
        cb.recordFailure(1003);
        assertEquals("OPEN", cb.state(1003));
    }

    @Test
    void trialFailureReopensWithNewTimer() {
        Solution.CircuitBreaker cb = new Solution.CircuitBreaker(1, 1000);
        cb.recordFailure(0);
        assertTrue(cb.allowRequest(1000));
        cb.recordFailure(1200);
        assertEquals("OPEN", cb.state(1200));
        assertEquals("OPEN", cb.state(2199));
        assertFalse(cb.allowRequest(2199));
        assertEquals("HALF_OPEN", cb.state(2200));
        assertTrue(cb.allowRequest(2200));
    }
}
