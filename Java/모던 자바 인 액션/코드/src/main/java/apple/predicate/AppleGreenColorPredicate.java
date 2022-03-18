package apple.predicate;

import apple.Apple;
import apple.Color;

public class AppleGreenColorPredicate implements ApplePredicate {

    @Override
    public boolean test(Apple apple) {
        return Color.GREEN.equals(apple.getColor());
    }
}
