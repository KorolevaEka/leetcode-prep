import java.util.List;

public class Solution {
    public record TestRun(String name, String status, int durationMs) {}

    public static List<String> slowPassed(List<TestRun> runs, int limitMs) {
        return runs.stream()
                .filter(r -> r.status().equals("PASSED"))
                .filter(r -> r.durationMs() >= limitMs)
                .map(TestRun::name)
                .sorted()
                .toList();
    }
}
