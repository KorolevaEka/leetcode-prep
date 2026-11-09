import java.util.List;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class SolutionTest {
    private static Solution.TestRun run(String name, String status, int ms) {
        return new Solution.TestRun(name, status, ms);
    }

    @Test
    @DisplayName("пример из условия")
    void example() {
        List<Solution.TestRun> runs = List.of(
                run("login", "PASSED", 900), run("cart", "PASSED", 300),
                run("pay", "FAILED", 5000), run("search", "PASSED", 1200));
        assertEquals(List.of("login", "search"), Solution.slowPassed(runs, 500));
    }

    @Test
    @DisplayName("граница строгая")
    void strictLimit() {
        assertEquals(List.of(), Solution.slowPassed(List.of(run("a", "PASSED", 500)), 500));
        assertEquals(List.of("a"), Solution.slowPassed(List.of(run("a", "PASSED", 501)), 500));
    }

    @Test
    @DisplayName("упавшие и пропущенные не попадают")
    void onlyPassed() {
        assertEquals(List.of(), Solution.slowPassed(List.of(run("a", "FAILED", 9000), run("b", "SKIPPED", 9000)), 100));
    }

    @Test
    @DisplayName("результат отсортирован по алфавиту")
    void sorted() {
        List<Solution.TestRun> runs = List.of(run("zeta", "PASSED", 10), run("alpha", "PASSED", 10), run("mid", "PASSED", 10));
        assertEquals(List.of("alpha", "mid", "zeta"), Solution.slowPassed(runs, 0));
    }

    @Test
    @DisplayName("пустой список и повторы")
    void emptyAndDuplicates() {
        assertEquals(List.of(), Solution.slowPassed(List.of(), 0));
        assertEquals(List.of("a", "a"), Solution.slowPassed(List.of(run("a", "PASSED", 5), run("a", "PASSED", 7)), 1));
    }
}
