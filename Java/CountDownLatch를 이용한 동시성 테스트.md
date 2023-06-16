# 학습 동기

여러 스레드에서 요청이 들어오는 경우에 대해서 테스트하기 위해서 Java에서 제공하는 Concurrency API의 CountDownLatch와 ExecutorService를 사용했습니다. 해당 클래스에 대해서 학습을 해보고 어떻게 작동하도록 설계했는지 소개하는 글을 작성하려고 합니다.

# CountDownLatch

## 역할

CountDownLatch는 쓰레드를 여러개 실행했을 때 모든 쓰레드의 작업이 끝나야지 다음으로 진행할 수 있거나 다른 쓰레드를 실행 시킬 수 있는 경우 사용합니다. 예를 들어서 Thread 5개를 실행시켰을 때 작업이 완료되어야 다음 작업이 진행되어야 하는 경우 사용할 수 있습니다.

작업이 끝날 때 `countDown()` 메서드를 호출하고 `await()` 메서드를 통해 countDown이 0가 됐을 때 다음 작업을 진행할 수 있도록 설정할 수 있습니다.



# ExecutorService

## 역할

여러 개의 작업을 효율적으로 처리하기 위한 Java의 라이브러리

ThreadPool을 이용해서 Task를 실행하고 관리한다.