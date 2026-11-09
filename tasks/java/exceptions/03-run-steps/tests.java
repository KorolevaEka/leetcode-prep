import java.util.ArrayList;
import java.util.List;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class SolutionTest {
    static class Recorded implements Solution.Step {
        private final String name;
        private final List<String> log;
        private final Exception runError;
        private final Exception undoError;

        Recorded(String name, List<String> log, Exception runError, Exception undoError) {
            this.name = name;
            this.log = log;
            this.runError = runError;
            this.undoError = undoError;
        }

        public String name() {
            return name;
        }

        public void run() throws Exception {
            log.add("run " + name);
            if (runError != null) {
                throw runError;
            }
        }

        public void undo() throws Exception {
            log.add("undo " + name);
            if (undoError != null) {
                throw undoError;
            }
        }
    }

    private static Solution.Step ok(String name, List<String> log) {
        return new Recorded(name, log, null, null);
    }

    @Test
    @DisplayName("все шаги прошли: отката нет")
    void allOk() {
        List<String> log = new ArrayList<>();
        Solution.runAll(List.of(ok("A", log), ok("B", log)));
        assertEquals(List.of("run A", "run B"), log);
    }

    @Test
    @DisplayName("пустой список шагов")
    void noSteps() {
        Solution.runAll(List.of());
    }

    @Test
    @DisplayName("откат в обратном порядке, упавший шаг не откатывается")
    void rollbackReverse() {
        List<String> log = new ArrayList<>();
        Solution.StepFailedException e = assertThrows(Solution.StepFailedException.class, () ->
                Solution.runAll(List.of(ok("A", log), ok("B", log), new Recorded("C", log, new IllegalStateException("boom"), null), ok("D", log))));
        assertEquals(List.of("run A", "run B", "run C", "undo B", "undo A"), log);
        assertEquals("C", e.getMessage());
    }

    @Test
    @DisplayName("причина сохраняется")
    void causeKept() {
        List<String> log = new ArrayList<>();
        IllegalStateException cause = new IllegalStateException("boom");
        Solution.StepFailedException e = assertThrows(Solution.StepFailedException.class, () ->
                Solution.runAll(List.of(new Recorded("A", log, cause, null))));
        assertTrue(cause == e.getCause());
        assertEquals(List.of("run A"), log);
    }

    @Test
    @DisplayName("ошибка отката не останавливает откат и попадает в suppressed")
    void undoFailure() {
        List<String> log = new ArrayList<>();
        Exception undoBoom = new RuntimeException("undo failed");
        Solution.StepFailedException e = assertThrows(Solution.StepFailedException.class, () ->
                Solution.runAll(List.of(ok("A", log), new Recorded("B", log, null, undoBoom), ok("C", log),
                        new Recorded("D", log, new RuntimeException("x"), null))));
        assertEquals(List.of("run A", "run B", "run C", "run D", "undo C", "undo B", "undo A"), log);
        assertEquals(1, e.getSuppressed().length);
        assertTrue(undoBoom == e.getSuppressed()[0]);
    }
}
