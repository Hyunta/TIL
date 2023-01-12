https://jypthemiracle.medium.com/java-stream-api는-왜-for-loop보다-느릴까-50dec4b9974b

[AngelikaLanger.com - Conference Video - GeeCon 2015 - The Performance Model of Streams in Java 8 - Angelika Langer - Angelika Langer Training/Consulting](http://www.angelikalanger.com/Conferences/Videos/Conference-Video-GeeCon-2015-Performance-Model-of-Streams-in-Java-8-Angelika-Langer.html)

Stream은 함수형 프로그래밍에서 이야기하는 sequence 와 동일한 말이다. sequence는 task의 순서를 나열한 것이다.

```java
음식을 배달시켜 먹는 프로세스
1. order()
2. deliver()
3. eat()
```

1,2,3번은 선행되는 행동에 종속적이다. sequence 대로 일을 처리하라고 하는 함수를 파라미터로 넘기는 행위를 sequential programming 이라고 한다.

GoF 디자인 패턴에 나오는 내부 반복자 패턴(Internal Iterator Pattern)과 동일하다.

> 컬렉션 내부에서 요소들을 반복시키고 개발자는 요소당 처리해야할 코드만 제공하는 패턴

처리해야 할 함수를 제공하면 Collection 순회를 외부에서 하는 것이 아니라 Stream 내부에서 하는 것이다.

스트림은 Object에 methodChaining을 하며 사용한다. 이를 보고 Fluent Programming이라고 부른다.

```java
deliveryDuties.stream()
							.filter()
							.collect()
```

스트림을 반환하는 함수를 중간 연산이라고 하고, 최종 결과물을 반환하는 collect를 최종 연산이라고 한다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c31d4180-17f5-44d1-b314-df7254ad1363/Untitled.png)

스트림을 반환하는 것은 연산의 파이프 라인을 반환한다는 의미다. 스트림은 Lazy한데, 매번 중간 연산마다 조건을 실행하지 않는다. 대신 중간 연산마다 연산의 파이프라인을 리턴한다. 최종 연산 과정에 들어와서야 값을 합쳐서 최종 연산에 돌입한다. Stream은 이미 존재하는 자료구조내에서 새로운 스트림을 생성할 뿐이지, 기존 데이터를 수정하거나 바꾸지 않는다.

## For-loop vs Stream

값을 비교하기 위해 500,000개의 int를 저장하는 배열을 만들고 가장 큰 원소를 찾는 값을 for문과 stream으로 만들어보자

```java
// for-loop
int[] a = ints;
int e = ints.length;
int m = Integer.MIN_VALUE;
for (int i = 0; i < e; i++) {
    if (a[i] > m) {
        m = a[i];
    }
}
// sequential stream
int m = Arrays.stream(ints)
							.reduce(Integer.MIN_VALUE, Math::max);
```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/93a3f905-f070-43dd-a52f-af11c1f4f535/Untitled.png)

스트림보다 for-loop가 압도적으로 빨랐다. 그 이유중에는 JIT Compiler가 for-loop을 오랫동안 다뤘기 때문에 internal optimization이 잘되어있다고 한다. 하지만 Stream은 2015년에 도입되어 아직 최적화가 덜 됐다고 한다.

원시값 int가 아닌 참조값 Integer를 이용해서 테스트를 하면 결과가 크게 차이나지 않는다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/37c772b2-d0e7-4582-b4df-000762505bb7/Untitled.png)

이는 참조값은 Heap 영역에 저장되기 때문에 itertation Cost가 비싸기때문에 최적화가 되더라도 성능이 안좋게 나온 것으로 보인다.

slowSin()이라는 오래 걸리는 함수를 통한 for문 실험

```java
// for-loop
int[] a = ints;
int e = a.length;
double m = Double.MIN_VALUE;for (int i = 0; i < e; i++) {
     double d = Sine.slowSin(a[i]);
     if (d > m) m = d;
}

// sequential stream
Arrays.stream(ints)
			.mapToDouble(Sine::slowSin)
			.reduce(Double.MIN_VALUE, Math::max);
```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c49d9793-beb9-4b32-9b53-d66f6a41bcfb/Untitled.png)

for문과 stream의 차이가 이제는 무의미해졌다. iteration cost와 functionality cost의 합이 충분히 클 때 stream과 for문의 차이는 줄어든다고 한다.

> Collections and streams, while bearing some superficial similarities, have different goals. Collections are primarily concerned with the efficient management of, and access to, their elements. By contrast, streams do not provide a means to directly access or manipulate their elements, and are instead concerned with declaratively describing their source and the computational operations which will be performed in aggregate on that source. However, if the provided stream operations do not offer the desired functionality, the `[BaseStream.iterator()](<https://docs.oracle.com/javase/8/docs/api/java/util/stream/BaseStream.html#iterator-->)` and `[BaseStream.spliterator()](<https://docs.oracle.com/javase/8/docs/api/java/util/stream/BaseStream.html#spliterator-->)` operations can be used to perform a controlled traversal.

컬렉션은 원소값의 편리성을 메인으로 본다면, 스트림은 원소 조작에 중점을 두고 함수형 스타일로 데이터를 처리한다.