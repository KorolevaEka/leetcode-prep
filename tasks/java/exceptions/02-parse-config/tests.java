import java.util.List;
import java.util.Map;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class SolutionTest {
    @Test
    @DisplayName("обычные строки, пробелы и комментарии")
    void valid() throws Exception {
        assertEquals(Map.of("host", "qa.local", "port", "8080"),
                Solution.parseConfig(List.of("host = qa.local", "", "# comment", "  port=8080  ")));
    }

    @Test
    @DisplayName("значение содержит знак равенства или пусто")
    void valueSpecial() throws Exception {
        assertEquals(Map.of("url", "http://x/?a=b", "token", ""),
                Solution.parseConfig(List.of("url=http://x/?a=b", "token=")));
    }

    @Test
    @DisplayName("пустой список")
    void empty() throws Exception {
        assertEquals(Map.of(), Solution.parseConfig(List.of()));
    }

    @Test
    @DisplayName("строка без знака равенства: номер строки с учётом пустых")
    void missingEquals() {
        Solution.ConfigException e = assertThrows(Solution.ConfigException.class,
                () -> Solution.parseConfig(List.of("a=1", "", "oops")));
        assertEquals("line 3", e.getMessage());
    }

    @Test
    @DisplayName("повторяющийся ключ")
    void duplicateKey() {
        Solution.ConfigException e = assertThrows(Solution.ConfigException.class,
                () -> Solution.parseConfig(List.of("a=1", "b=2", "a=3")));
        assertEquals("line 3", e.getMessage());
    }

    @Test
    @DisplayName("пустой ключ")
    void emptyKey() {
        Solution.ConfigException e = assertThrows(Solution.ConfigException.class,
                () -> Solution.parseConfig(List.of("# header", "=value")));
        assertEquals("line 2", e.getMessage());
    }

    @Test
    @DisplayName("закомментированная строка без равенства не ошибка")
    void commentWithoutEquals() throws Exception {
        assertEquals(Map.of("a", "1"), Solution.parseConfig(List.of("# just a note", "a=1")));
    }
}
