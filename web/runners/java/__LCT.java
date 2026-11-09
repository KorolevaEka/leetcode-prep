// Сторож зацикливания: браузерный исполнитель вставляет __LCT.tick() в циклы и методы кода пользователя.
public final class __LCT {
    static volatile long deadline = Long.MAX_VALUE;
    private static int n;

    public static boolean tick() {
        if ((++n & 1023) == 0 && System.currentTimeMillis() > deadline) {
            System.out.println("\nТаймаут: решение работает слишком долго (бесконечный цикл?)");
            System.out.flush();
            Runtime.getRuntime().halt(124);
        }
        return true;
    }
}
