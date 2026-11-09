import java.util.List;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class SolutionTest {
    @Test
    @DisplayName("пример из условия")
    void example() {
        assertEquals(List.of("b", "a"), Solution.topFailing(List.of("b", "a", "b", "c", "a", "b"), 2));
    }

    @Test
    @DisplayName("равное число падений: по алфавиту")
    void tiesAlphabetical() {
        assertEquals(List.of("x", "y"), Solution.topFailing(List.of("z", "y", "x"), 2));
    }

    @Test
    @DisplayName("n больше числа тестов")
    void nTooBig() {
        assertEquals(List.of("a"), Solution.topFailing(List.of("a"), 5));
        assertEquals(List.of("q", "p"), Solution.topFailing(List.of("p", "q", "q"), 10));
    }

    @Test
    @DisplayName("n = 0 и отрицательное n")
    void nonPositive() {
        assertEquals(List.of(), Solution.topFailing(List.of("a", "b"), 0));
        assertEquals(List.of(), Solution.topFailing(List.of("a", "b"), -1));
    }

    @Test
    @DisplayName("пустой список")
    void empty() {
        assertEquals(List.of(), Solution.topFailing(List.of(), 3));
    }

    @Test
    @DisplayName("порядок: частота важнее алфавита")
    void countBeforeName() {
        assertEquals(List.of("login", "cart", "alpha"),
                Solution.topFailing(List.of("alpha", "cart", "login", "login", "cart", "login"), 3));
    }
}
