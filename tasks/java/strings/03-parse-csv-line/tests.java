import java.util.List;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class SolutionTest {
    @Test
    @DisplayName("простые поля")
    void plain() {
        assertEquals(List.of("id", "name", "status"), Solution.parseCsvLine("id,name,status"));
    }

    @Test
    @DisplayName("запятая внутри кавычек")
    void commaInQuotes() {
        assertEquals(List.of("7", "Smith, John", "ok"), Solution.parseCsvLine("7,\"Smith, John\",ok"));
    }

    @Test
    @DisplayName("удвоенная кавычка внутри поля")
    void escapedQuote() {
        assertEquals(List.of("1", "say \"hi\"", "", ""), Solution.parseCsvLine("1,\"say \"\"hi\"\"\",,"));
    }

    @Test
    @DisplayName("пустые поля и пустая строка")
    void empties() {
        assertEquals(List.of("a", "", "c"), Solution.parseCsvLine("a,,c"));
        assertEquals(List.of("a", "b", ""), Solution.parseCsvLine("a,b,"));
        assertEquals(List.of(""), Solution.parseCsvLine(""));
    }

    @Test
    @DisplayName("пробелы сохраняются")
    void spacesKept() {
        assertEquals(List.of(" a ", " b"), Solution.parseCsvLine(" a , b"));
    }

    @Test
    @DisplayName("пустое поле в кавычках")
    void emptyQuoted() {
        assertEquals(List.of("", "x"), Solution.parseCsvLine("\"\",x"));
    }

    @Test
    @DisplayName("единственное поле в кавычках")
    void singleQuoted() {
        assertEquals(List.of("a,b"), Solution.parseCsvLine("\"a,b\""));
    }
}
