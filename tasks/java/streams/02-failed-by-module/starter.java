import java.util.List;
import java.util.Map;

public class Solution {
    public record TestRun(String name, String status, int durationMs) {}

    public static Map<String, Long> failedByModule(List<TestRun> runs) {
        throw new UnsupportedOperationException("TODO");
    }
}
