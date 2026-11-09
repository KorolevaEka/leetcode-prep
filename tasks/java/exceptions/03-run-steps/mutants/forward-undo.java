import java.util.ArrayList;
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
        List<Step> done = new ArrayList<>();
        for (Step step : steps) {
            try {
                step.run();
                done.add(step);
            } catch (Exception e) {
                StepFailedException failure = new StepFailedException(step.name(), e);
                for (int i = 0; i < done.size(); i++) {
                    try {
                        done.get(i).undo();
                    } catch (Exception undoError) {
                        failure.addSuppressed(undoError);
                    }
                }
                throw failure;
            }
        }
    }
}
