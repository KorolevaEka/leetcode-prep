import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class SolutionTest {
    private static final int[] LOG = {10, 20, 20, 30};

    @Test
    @DisplayName("первое из повторяющихся значений")
    void firstOfDuplicates() {
        assertEquals(1, Solution.firstAtLeast(LOG, 20));
    }

    @Test
    @DisplayName("значения между элементами")
    void between() {
        assertEquals(3, Solution.firstAtLeast(LOG, 25));
        assertEquals(1, Solution.firstAtLeast(LOG, 11));
    }

    @Test
    @DisplayName("цель больше всех: длина массива")
    void beyondEnd() {
        assertEquals(4, Solution.firstAtLeast(LOG, 99));
        assertEquals(4, Solution.firstAtLeast(LOG, 31));
    }

    @Test
    @DisplayName("цель меньше всех или равна первому")
    void beforeStart() {
        assertEquals(0, Solution.firstAtLeast(LOG, -5));
        assertEquals(0, Solution.firstAtLeast(LOG, 10));
    }

    @Test
    @DisplayName("последний элемент найден")
    void lastElement() {
        assertEquals(3, Solution.firstAtLeast(LOG, 30));
    }

    @Test
    @DisplayName("пустой массив и один элемент")
    void tiny() {
        assertEquals(0, Solution.firstAtLeast(new int[] {}, 5));
        assertEquals(0, Solution.firstAtLeast(new int[] {7}, 7));
        assertEquals(1, Solution.firstAtLeast(new int[] {7}, 8));
    }

    @Test
    @DisplayName("все элементы равны")
    void allEqual() {
        assertEquals(0, Solution.firstAtLeast(new int[] {5, 5, 5, 5, 5}, 5));
        assertEquals(5, Solution.firstAtLeast(new int[] {5, 5, 5, 5, 5}, 6));
    }
}
