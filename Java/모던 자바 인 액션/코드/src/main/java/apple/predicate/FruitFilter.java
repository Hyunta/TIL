package apple.predicate;

import java.util.ArrayList;
import java.util.List;
import java.util.function.Predicate;

public class FruitFilter {

    public static <T> List<T> filter(List<T> list, Predicate<T> predicate) {
        List<T> result = new ArrayList<>();
        for (T e : list) {
            if (predicate.test(e)) {
                result.add(e);
            }
        }
        return result;
    }
}
