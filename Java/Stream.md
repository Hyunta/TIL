## 소개

스트림은 람다를 활용할 수 있는 기술 중 하나입니다.

JDK8 이전에는 컬렉션을 다루는 방법은 for 또는 foreach 문을 돌면서 요소 하나씩을 꺼내서 다루는 것이었습니다.

간단한 경우라면 상관없지만 로직이 복잡해질수록 유지보수가 어려워집니다.



스트림을 이용하면 배열과 컬렉션을 함수형으로 처리할 수 있기 때문에 보다 간결하게 표현할 수 있습니다.

또한 병렬처리가 가능하기 때문에 빠르게 처리가 가능합니다.



## 특징

- 원본 데이터에 변형을 가하지 않는다.
- 함수형으로 코드를 간결하게 작성할 수 있다.
- 일회용이다.
- 내부 반복으로 작업을 처리한다.



## 연산 종류

1. 생성하기

   Stream 객체를 생성하는 단계 

   재사용이 불가능하므로, 닫히면 다시 생성해줘야 한다.

2. 가공하기

   원본 데이터를 별도의 데이터로 가공하기 위한 연산

   결과를 Stream으로 반환하기 때문에 계속해서 중간 연산을 이어갈 수 있다

3. 결과만들기

   원하는 결과를 만들기 위한 연산

   1번만 수행 가능하다.



## 람다식

Stream 연산들은 매개변수로 함수형 인터페이스를 받도록 되어있다. 

람다식은 반환값으로 함수형 인터페이스를 반환하고 있다.



람다식이란?

함수를 하나의 식으로 표현한 것이다. 메서드의 이름이 필요없기 때문에 익명 함수의 한 종류라고 볼 수 있다.

불필요한 코드를 줄이고 가독성을 높이기 위해 등장했다.



## 함수형 인터페이스

람다식으로 순수 함수를 선언할 수 있게 됐다. Java에서 순수 함수와 일반 함수를 구분하기 위해 등장했다.

함수를 1급 객체처럼 다룰 수 있게 하는 어노테이션, 인터페이스에 선언하여 단 하나의 추상 메서드만을 갖도록 제한하는 역할



### Java에서 제공하는 함수형 인터페이스

1. Supplier<T>

   매개변수 없이 반환값 만을 갖는 함수형 인터페이스

2. Consumer<T>

   객체 T를 매개변수로 받아서 사용하며, 반환값은 없는 함수형 인터페이스

3. Function<T,R>

   객체 T를 매개변수로 받아서 처리한 후 R로 반환하는 함수형 인터페이스다.

4. Predicate<T>

   객체 T를 매개변수로 받아 처리한 후 Boolean을 반환한다.





## 스트림 생성하기

1. Collection

   Collection 인터페이스에는 stream이 정의되어 있기 때문에 구현체들은 이를 통해 stream을 생성할 수 있다.

2. 배열

   Strem.of 또는 Arrays.stream()

3. 원시 Stream 생성

   IntStream, LongStream, DoubleStream



## 스트림 가공하기

1. Filter
2. Map
3. Sorted
4. Distinct
5. peek



## 스트림 결과 만들기

1. Max, Min, Sum, Avg, Count
2. collect
   - List, Set, Map



## Parallel Stream 활용

런타임 성능을 높이기 위해 병렬로 실행가능한 Parallel Stream을 제공하고 있다.

내부적으로 fork & join을 사용하고, ForkJoinPool.commonPool()을 통해 사용가능한 ForkJoinPool의 개수를 확인할 수 있다.