package apple;

import static apple.Color.*;

import apple.predicate.AppleHeavyWeightPredicate;
import apple.predicate.FruitFilter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Application {
    public static void main(String[] args) {
        List<Apple> inventory = Arrays.asList(
                new Apple(GREEN, 180),
                new Apple(RED, 70));
//        List<Apple> apples = AppleFilter.filterApples(inventory, new AppleHeavyWeightPredicate());
//        System.out.println(apples);

        List<Apple> apples = AppleFilter.filterApples(inventory, (Apple apple) -> RED.equals(apple.getColor()));
        System.out.println(apples);

        List<Integer> numbers = IntStream.range(0, 10).boxed().collect(Collectors.toList());
        List<Integer> evenNumbers = FruitFilter.filter(numbers, (Integer i) -> i % 2 == 0);
        System.out.println(evenNumbers);
    }
}
