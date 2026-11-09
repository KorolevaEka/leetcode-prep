import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class SolutionTest {
    @Test
    void bytesBelowOneKilobyte() {
        assertEquals("0 B", Solution.formatSize(0));
        assertEquals("512 B", Solution.formatSize(512));
        assertEquals("1023 B", Solution.formatSize(1023));
    }

    @Test
    void kilobytes() {
        assertEquals("1.0 KB", Solution.formatSize(1024));
        assertEquals("1.5 KB", Solution.formatSize(1536));
    }

    @Test
    void fractionIsTruncatedNotRounded() {
        assertEquals("1023.9 KB", Solution.formatSize(1048575));
        assertEquals("1.0 KB", Solution.formatSize(1024 + 50));
    }

    @Test
    void megabytes() {
        assertEquals("1.0 MB", Solution.formatSize(1048576));
        assertEquals("2.5 MB", Solution.formatSize(2621440));
    }

    @Test
    void gigabytesAndBeyond() {
        assertEquals("1.0 GB", Solution.formatSize(1073741824L));
        assertEquals("2048.0 GB", Solution.formatSize(2199023255552L));
    }

    @Test
    void negativeSize() {
        assertThrows(IllegalArgumentException.class, () -> Solution.formatSize(-1));
    }
}
