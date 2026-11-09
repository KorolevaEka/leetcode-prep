import java.util.List;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class SolutionTest {
    @Test
    @DisplayName("перекрывающиеся вхождения")
    void overlapping() {
        assertEquals(List.of(0, 1, 2), Solution.findAll("aaaa", "aa"));
    }

    @Test
    @DisplayName("несколько вхождений")
    void several() {
        assertEquals(List.of(0, 7), Solution.findAll("ERR ok ERR", "ERR"));
    }

    @Test
    @DisplayName("вхождение в самом конце")
    void atEnd() {
        assertEquals(List.of(3), Solution.findAll("abcxyz", "xyz"));
        assertEquals(List.of(2), Solution.findAll("abc", "c").subList(0, 1));
    }

    @Test
    @DisplayName("нет вхождений и шаблон длиннее текста")
    void none() {
        assertEquals(List.of(), Solution.findAll("abc", "x"));
        assertEquals(List.of(), Solution.findAll("ab", "abc"));
        assertEquals(List.of(), Solution.findAll("", "a"));
    }

    @Test
    @DisplayName("регистр важен")
    void caseSensitive() {
        assertEquals(List.of(6), Solution.findAll("Error error", "error"));
    }

    @Test
    @DisplayName("шаблон совпадает с текстом целиком")
    void wholeText() {
        assertEquals(List.of(0), Solution.findAll("abc", "abc"));
    }

    @Test
    @DisplayName("пустой шаблон")
    void emptyPattern() {
        assertThrows(IllegalArgumentException.class, () -> Solution.findAll("abc", ""));
    }
}
