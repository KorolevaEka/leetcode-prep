import java.util.List;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class SolutionTest {
    private static Solution.TestRun run(String name, String status) {
        return new Solution.TestRun(name, status, 50);
    }

    @Test
    @DisplayName("пример из условия")
    void example() {
        List<List<Solution.TestRun>> attempts = List.of(
                List.of(run("login", "FAILED"), run("cart", "PASSED"), run("pay", "FAILED")),
                List.of(run("login", "PASSED"), run("cart", "PASSED"), run("pay", "FAILED")));
        assertEquals(List.of("login"), Solution.flakyTests(attempts));
    }

    @Test
    @DisplayName("стабильные тесты не попадают")
    void stableOnly() {
        List<List<Solution.TestRun>> attempts = List.of(
                List.of(run("a", "PASSED"), run("b", "FAILED")),
                List.of(run("a", "PASSED"), run("b", "FAILED")),
                List.of(run("a", "PASSED"), run("b", "FAILED")));
        assertEquals(List.of(), Solution.flakyTests(attempts));
    }

    @Test
    @DisplayName("SKIPPED не делает тест нестабильным")
    void skippedIgnored() {
        List<List<Solution.TestRun>> attempts = List.of(
                List.of(run("a", "SKIPPED"), run("b", "SKIPPED")),
                List.of(run("a", "PASSED"), run("b", "FAILED")));
        assertEquals(List.of(), Solution.flakyTests(attempts));
    }

    @Test
    @DisplayName("отсортировано, без повторов")
    void sortedUnique() {
        List<List<Solution.TestRun>> attempts = List.of(
                List.of(run("zeta", "FAILED"), run("alpha", "PASSED")),
                List.of(run("zeta", "PASSED"), run("alpha", "FAILED")),
                List.of(run("zeta", "FAILED"), run("alpha", "PASSED")));
        assertEquals(List.of("alpha", "zeta"), Solution.flakyTests(attempts));
    }

    @Test
    @DisplayName("пустые входные данные")
    void empty() {
        assertEquals(List.of(), Solution.flakyTests(List.of()));
        assertEquals(List.of(), Solution.flakyTests(List.of(List.of(), List.of())));
    }

    @Test
    @DisplayName("одна попытка не может дать нестабильность")
    void singleAttempt() {
        assertEquals(List.of(), Solution.flakyTests(List.of(List.of(run("a", "PASSED"), run("b", "FAILED")))));
    }
}
