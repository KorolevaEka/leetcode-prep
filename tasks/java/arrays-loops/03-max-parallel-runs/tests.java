import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class SolutionTest {
    @Test
    @DisplayName("пример из условия")
    void example() {
        assertEquals(2, Solution.maxParallel(new int[][] {{0, 5}, {2, 6}, {5, 8}}));
    }

    @Test
    @DisplayName("пустой ввод и один прогон")
    void tiny() {
        assertEquals(0, Solution.maxParallel(new int[][] {}));
        assertEquals(1, Solution.maxParallel(new int[][] {{3, 4}}));
    }

    @Test
    @DisplayName("прогоны встык не пересекаются")
    void touching() {
        assertEquals(1, Solution.maxParallel(new int[][] {{0, 1}, {1, 2}, {2, 3}}));
    }

    @Test
    @DisplayName("все прогоны одновременно")
    void allAtOnce() {
        assertEquals(3, Solution.maxParallel(new int[][] {{0, 10}, {0, 10}, {0, 10}}));
    }

    @Test
    @DisplayName("неотсортированный ввод и вложенные прогоны")
    void unsortedNested() {
        assertEquals(3, Solution.maxParallel(new int[][] {{10, 12}, {0, 11}, {1, 3}, {2, 4}}));
    }

    @Test
    @DisplayName("пик не в конце")
    void peakInMiddle() {
        assertEquals(3, Solution.maxParallel(new int[][] {{1, 4}, {2, 5}, {3, 6}, {7, 8}, {9, 10}}));
    }

    @Test
    @DisplayName("отрицательные времена")
    void negativeTimes() {
        assertEquals(2, Solution.maxParallel(new int[][] {{-5, -1}, {-3, 2}, {2, 4}}));
    }
}
