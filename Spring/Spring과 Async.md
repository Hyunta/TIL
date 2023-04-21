# `@Async 와 Spring`

https://www.youtube.com/watch?v=HKlUvCv9hvA

스프링에서 비동기가 어떻게 이뤄지는지 소개하는 자리

1. 자바 비동기 개발을 알고 있어야 한다.
   1. 자바 5+
      - Future / Executor
      - BlockingQueue
   2. 자바 7
      - ForkJoinTask
   3. 자바 8
      - CompletableFuture
   4. 자바 9
      - Flow
2. 서블릿 비동기 개발을 알아야 한다
   - Sevlet 3.0 Async Processing
     - AsyncContext
3. 스프링 비동기 개발
   1. `@Async`
   2. Async Request Processing
   3. AsyncRestTemplate

------

Singleton - 1

Dependency Injection -3 / Configuration, 주입자, 피주입자

Synchronous / Asynchronous :

시간을 맞추는 / 시간을 맞추지 않는

A와 B가 시작시간 또는 종료시간이 일치하면 동기

- A,B 쓰레드가 동시에 작업을 시작하면 동기(CyclicBarrier)
- 메서드 리턴시간(A)과 결과를 전달받는 시간(B)가 일치하면 동기

A가 끝나는 시간과 B가 시작하는 시간이 같으면 동기

- synchronized
- BlockingQueue

블로킹, 논블로킹

- 동기, 비동기와 관점이 다름
- 내가 직접 제어할 수 없는 대상을 상대하는 방법
- 대상이 제한적임
  - IO
  - 멀티 쓰레드 동기화

스프링에서는 `@Async` 로 비동기 처리

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b04f67ac-322f-4da3-9a65-f9dfbacf6151/Untitled.png)

일반 String은 Async가 지원하지 않는다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7257eb60-6b81-45e7-8729-f65c2fa02537/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b954394b-9b05-4c2e-94b6-4b7f0c57fec4/Untitled.png)

- Future는 Java 비동기의 결과를 가져오는 기본적인 인터페이스

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/65f2bf50-2af3-4f1c-9a2f-210c4e6f4c10/Untitled.png)

- ListenableFuture은 Spring에서 callback을 추가해서 만들면 된다.
- non-blocking으로 받을 수 있다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0d7dcce3-ecae-4873-8483-8eec1642dca0/Untitled.png)

- Java 8 부터 나온 CompletableFuture
- CompletedFuture 이라는 static method가 있다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/67b1cbda-240d-4ccd-82dc-9d4135eb0a4b/Untitled.png)

- Spring이 기본으로 등록해둔 값을 사용한다.
- 단점은 새로운 스레드를 만들고, 버리는 과정을 반복하는 것이다.
- 스레드를 낭비하게 된다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/27c2808d-db1e-47c0-9905-c3ab06cfbaff/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/65a3f8a1-4979-4863-b0b0-04a452565fd6/Untitled.png)

- threadPool은 CorePool 만큼만 채우고 이후에는 Queue를 채운다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/18fae280-5d31-4fdc-afa2-d1a21220a75c/Untitled.png)

- 약 2009년에 출시

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d66a8f48-8705-4145-b705-f5f686ef8be1/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/125bb0ca-e0e2-45dc-a886-7f6e6c681f67/Untitled.png)

- ListenableFuture의 문제점 이것을 해결하기 위해 CompletableFuture이 나왔다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/eee2f743-bab8-456d-89d9-830a4d44f6f1/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9895ac38-f998-4f0b-9303-7bc22ed9b053/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b8c7e4f3-0eb2-4d0f-ad3a-a1e8d600254a/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/28c53afd-8519-4cd0-be92-e43d9a3583c2/Untitled.png)

- AsyncRestTemplate을 가지고 왔다.