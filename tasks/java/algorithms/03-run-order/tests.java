import java.util.List;
import java.util.Map;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class SolutionTest {
    @Test
    @DisplayName("цепочка и независимая задача")
    void chain() {
        Map<String, List<String>> deps = Map.of("report", List.of("tests"), "tests", List.of("build"), "lint", List.of());
        assertEquals(List.of("build", "lint", "tests", "report"), Solution.runOrder(deps));
    }

    @Test
    @DisplayName("при равенстве — по алфавиту")
    void alphabeticalTies() {
        assertEquals(List.of("a", "b", "c"), Solution.runOrder(Map.of("b", List.of("a"), "c", List.of())));
        assertEquals(List.of("a", "m", "z"), Solution.runOrder(Map.of("z", List.of(), "a", List.of(), "m", List.of())));
    }

    @Test
    @DisplayName("задача, указанная только в зависимостях")
    void dependencyOnly() {
        assertEquals(List.of("tests", "report"), Solution.runOrder(Map.of("report", List.of("tests"))));
    }

    @Test
    @DisplayName("ромб зависимостей")
    void diamond() {
        Map<String, List<String>> deps = Map.of(
                "deploy", List.of("api", "web"), "api", List.of("build"), "web", List.of("build"), "build", List.of());
        assertEquals(List.of("build", "api", "web", "deploy"), Solution.runOrder(deps));
    }

    @Test
    @DisplayName("цикл")
    void cycle() {
        assertThrows(IllegalStateException.class, () -> Solution.runOrder(Map.of("a", List.of("b"), "b", List.of("a"))));
        assertThrows(IllegalStateException.class,
                () -> Solution.runOrder(Map.of("x", List.of(), "a", List.of("b"), "b", List.of("c"), "c", List.of("a"))));
    }

    @Test
    @DisplayName("зависимость от самой себя")
    void selfDependency() {
        assertThrows(IllegalStateException.class, () -> Solution.runOrder(Map.of("a", List.of("a"))));
    }

    @Test
    @DisplayName("пустая карта")
    void empty() {
        assertEquals(List.of(), Solution.runOrder(Map.of()));
    }
}
