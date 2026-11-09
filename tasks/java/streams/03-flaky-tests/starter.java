import java.util.List;

public class Solution {
    public record TestRun(String name, String status, int durationMs) {}

    public static List<String> flakyTests(List<List<TestRun>> attempts) {
        throw new UnsupportedOperationException("TODO");
    }
}
