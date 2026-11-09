import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class SolutionTest {
    private static Solution.TestRun run(String name, String status) {
        return new Solution.TestRun(name, status, 100);
    }

    @Test
    @DisplayName("пример из условия")
    void example() {
        List<Solution.TestRun> runs = List.of(
                run("auth.login_ok", "FAILED"), run("auth.logout", "PASSED"), run("cart.add.item", "FAILED"),
                run("cart.remove", "FAILED"), run("smoke", "FAILED"));
        assertEquals(Map.of("auth", 1L, "cart", 2L, "smoke", 1L), Solution.failedByModule(runs));
    }

    @Test
    @DisplayName("ключи идут по алфавиту")
    void keysSorted() {
        List<Solution.TestRun> runs = List.of(
                run("search.q", "FAILED"), run("payments.p", "FAILED"), run("auth.a", "FAILED"),
                run("cart.c", "FAILED"), run("profile.p", "FAILED"), run("admin.a", "FAILED"));
        assertEquals(List.of("admin", "auth", "cart", "payments", "profile", "search"),
                new ArrayList<>(Solution.failedByModule(runs).keySet()));
    }

    @Test
    @DisplayName("модуль — до первой точки")
    void firstDot() {
        List<Solution.TestRun> runs = List.of(run("api.v1.users", "FAILED"), run("api.v2.users", "FAILED"));
        assertEquals(Map.of("api", 2L), Solution.failedByModule(runs));
    }

    @Test
    @DisplayName("модули без падений отсутствуют")
    void noFailures() {
        assertEquals(Map.of(), Solution.failedByModule(List.of(run("auth.a", "PASSED"), run("cart.b", "SKIPPED"))));
        assertEquals(Map.of(), Solution.failedByModule(List.of()));
    }

    @Test
    @DisplayName("пропущенные не считаются падениями")
    void skippedNotCounted() {
        List<Solution.TestRun> runs = List.of(run("ui.a", "SKIPPED"), run("ui.b", "FAILED"), run("ui.c", "PASSED"));
        assertEquals(Map.of("ui", 1L), Solution.failedByModule(runs));
    }
}
