import java.util.List;
import java.util.Map;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class SolutionTest {
    @Test
    @DisplayName("пример из условия")
    void example() {
        assertEquals(Map.of("PASSED", 2, "FAILED", 1), Solution.countStatuses(List.of("PASSED", "FAILED", "PASSED")));
    }

    @Test
    @DisplayName("пустой список")
    void empty() {
        assertEquals(Map.of(), Solution.countStatuses(List.of()));
    }

    @Test
    @DisplayName("один статус много раз")
    void sameStatus() {
        assertEquals(Map.of("FAILED", 4), Solution.countStatuses(List.of("FAILED", "FAILED", "FAILED", "FAILED")));
    }

    @Test
    @DisplayName("регистр различается")
    void caseSensitive() {
        assertEquals(Map.of("PASSED", 1, "passed", 2), Solution.countStatuses(List.of("passed", "PASSED", "passed")));
    }

    @Test
    @DisplayName("несколько разных статусов")
    void mixed() {
        assertEquals(Map.of("PASSED", 1, "FAILED", 2, "SKIPPED", 1),
                Solution.countStatuses(List.of("SKIPPED", "FAILED", "PASSED", "FAILED")));
    }
}
