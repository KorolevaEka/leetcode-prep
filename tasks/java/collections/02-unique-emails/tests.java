import java.util.List;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class SolutionTest {
    @Test
    @DisplayName("точные дубликаты")
    void exactDuplicates() {
        assertEquals(List.of("a@x.io", "b@x.io"), Solution.uniqueEmails(List.of("a@x.io", "b@x.io", "a@x.io", "b@x.io")));
    }

    @Test
    @DisplayName("дубликаты в другом регистре: остаётся первый")
    void caseInsensitive() {
        assertEquals(List.of("Zed@x.io", "amy@x.io"), Solution.uniqueEmails(List.of("Zed@x.io", "amy@x.io", "zed@x.io")));
    }

    @Test
    @DisplayName("порядок не сортируется")
    void keepsOrder() {
        assertEquals(List.of("m@x.io", "c@x.io", "x@x.io"), Solution.uniqueEmails(List.of("m@x.io", "c@x.io", "x@x.io", "C@x.io")));
    }

    @Test
    @DisplayName("пустой список и один адрес")
    void tiny() {
        assertEquals(List.of(), Solution.uniqueEmails(List.of()));
        assertEquals(List.of("one@x.io"), Solution.uniqueEmails(List.of("one@x.io")));
    }

    @Test
    @DisplayName("первое вхождение остаётся на своём месте")
    void firstWins() {
        assertEquals(List.of("B@x.io", "a@x.io"), Solution.uniqueEmails(List.of("B@x.io", "a@x.io", "b@x.io", "A@x.io")));
    }
}
