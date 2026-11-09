import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

public class Solution {
    public record TestRun(String name, String status, int durationMs) {}

    public static List<String> flakyTests(List<List<TestRun>> attempts) {
        return attempts.stream()
                .flatMap(List::stream)
                .collect(Collectors.groupingBy(TestRun::name, Collectors.mapping(TestRun::status, Collectors.toSet())))
                .entrySet().stream()
                .filter(e -> e.getValue().contains("PASSED") && e.getValue().contains("FAILED"))
                .map(Map.Entry::getKey)
                .sorted(java.util.Comparator.reverseOrder())
                .toList();
    }
}
