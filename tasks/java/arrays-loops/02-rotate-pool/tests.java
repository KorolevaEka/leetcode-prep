import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class SolutionTest {
    @Test
    @DisplayName("сдвиг вправо")
    void right() {
        assertArrayEquals(new int[] {4, 5, 1, 2, 3}, Solution.rotateRight(new int[] {1, 2, 3, 4, 5}, 2));
    }

    @Test
    @DisplayName("ноль: массив не меняется")
    void zero() {
        assertArrayEquals(new int[] {1, 2, 3}, Solution.rotateRight(new int[] {1, 2, 3}, 0));
    }

    @Test
    @DisplayName("сдвиг больше длины")
    void bigShift() {
        assertArrayEquals(new int[] {3, 1, 2}, Solution.rotateRight(new int[] {1, 2, 3}, 7));
        assertArrayEquals(new int[] {1, 2, 3}, Solution.rotateRight(new int[] {1, 2, 3}, 3));
    }

    @Test
    @DisplayName("отрицательный сдвиг — влево")
    void negative() {
        assertArrayEquals(new int[] {2, 3, 4, 5, 1}, Solution.rotateRight(new int[] {1, 2, 3, 4, 5}, -1));
        assertArrayEquals(new int[] {3, 1, 2}, Solution.rotateRight(new int[] {1, 2, 3}, -5));
    }

    @Test
    @DisplayName("пустой и одноэлементный массив")
    void tiny() {
        assertArrayEquals(new int[] {}, Solution.rotateRight(new int[] {}, 4));
        assertArrayEquals(new int[] {9}, Solution.rotateRight(new int[] {9}, 3));
    }

    @Test
    @DisplayName("исходный массив не меняется")
    void inputUntouched() {
        int[] input = {1, 2, 3, 4};
        Solution.rotateRight(input, 1);
        assertArrayEquals(new int[] {1, 2, 3, 4}, input);
    }
}
