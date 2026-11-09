import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class SolutionTest {
    @Test
    @DisplayName("пример из условия")
    void example() {
        assertArrayEquals(new int[] {300, 420, 500}, Solution.runningTotals(new int[] {300, 120, 80}));
    }

    @Test
    @DisplayName("пустой массив")
    void empty() {
        assertArrayEquals(new int[] {}, Solution.runningTotals(new int[] {}));
    }

    @Test
    @DisplayName("один элемент")
    void single() {
        assertArrayEquals(new int[] {42}, Solution.runningTotals(new int[] {42}));
    }

    @Test
    @DisplayName("нули и повторы")
    void zeros() {
        assertArrayEquals(new int[] {0, 5, 5, 10}, Solution.runningTotals(new int[] {0, 5, 0, 5}));
    }

    @Test
    @DisplayName("исходный массив не меняется")
    void inputUntouched() {
        int[] input = {1, 2, 3};
        Solution.runningTotals(input);
        assertArrayEquals(new int[] {1, 2, 3}, input);
    }
}
