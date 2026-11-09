import java.io.File;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.lang.reflect.Modifier;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

// Мини-JUnit: запускает методы @Test класса SolutionTest. Код выхода: 0 — всё прошло, 1 — есть падения, 5 — нет тестов.
public class TestRunner {
    public static void main(String[] args) throws Exception {
        __LCT.deadline = System.currentTimeMillis() + 9_000;
        if (args.length > 0) cleanSiblings(new File(args[0]));
        Class<?> cls;
        try {
            cls = Class.forName("SolutionTest");
        } catch (ClassNotFoundException e) {
            System.out.println("Нет ни одного теста: класс SolutionTest не найден");
            System.exit(5);
            return;
        }
        List<Method> tests = new ArrayList<>(), before = new ArrayList<>();
        for (Method m : cls.getDeclaredMethods()) {
            if (m.isAnnotationPresent(Test.class)) tests.add(m);
            if (m.isAnnotationPresent(BeforeEach.class)) before.add(m);
        }
        before.sort(Comparator.comparing(Method::getName));
        if (tests.isEmpty()) {
            System.out.println("No tests found");
            System.exit(5);
        }
        tests.sort(Comparator.comparing(Method::getName));
        var ctor = cls.getDeclaredConstructor();
        ctor.setAccessible(true);
        int passed = 0, failed = 0;
        for (Method m : tests) {
            DisplayName dn = m.getAnnotation(DisplayName.class);
            String name = dn != null ? dn.value() : m.getName();
            try {
                m.setAccessible(true);
                Object self = ctor.newInstance();
                for (Method b : before) {
                    b.setAccessible(true);
                    b.invoke(Modifier.isStatic(b.getModifiers()) ? null : self);
                }
                m.invoke(Modifier.isStatic(m.getModifiers()) ? null : self);
                passed++;
                System.out.println("✓ " + name);
            } catch (Throwable t) {
                if (t instanceof InvocationTargetException ite) t = ite.getCause();
                failed++;
                System.out.println("✕ " + name);
                System.out.println(describe(t).replaceAll("(?m)^", "    "));
            }
        }
        System.out.println("\nTests: " + (failed > 0 ? failed + " failed, " : "") + passed + " passed");
        System.out.flush();
        System.exit(failed > 0 ? 1 : 0);
    }

    private static String describe(Throwable t) {
        StringBuilder sb = new StringBuilder(t instanceof AssertionError ? String.valueOf(t.getMessage()) : t.toString());
        if (!(t instanceof AssertionError)) {
            for (StackTraceElement e : t.getStackTrace()) {
                String c = e.getClassName();
                if (c.startsWith("Solution")) sb.append("\n    at ").append(e);
            }
        }
        return sb.toString();
    }

    // В браузере каждый запуск компилирует в свою папку; старые папки удаляем, чтобы не копились.
    private static void cleanSiblings(File own) {
        File[] dirs = own.getAbsoluteFile().getParentFile().listFiles();
        if (dirs == null) return;
        for (File d : dirs) if (!d.getName().equals(own.getName())) delete(d);
    }

    private static void delete(File f) {
        File[] kids = f.listFiles();
        if (kids != null) for (File k : kids) delete(k);
        f.delete();
    }
}
