import java.util.List;

public class Solution {
    public interface Step {
        String name();

        void run() throws Exception;

        void undo() throws Exception;
    }

    public static class StepFailedException extends RuntimeException {
        public StepFailedException(String message, Throwable cause) {
            super(message, cause);
        }
    }

    public static void runAll(List<Step> steps) {
        throw new UnsupportedOperationException("TODO");
    }
}
