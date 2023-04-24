survivor0 과 1 중 하나는 비어있어야 한다.

age가 임계값이 넘을경우 Old 로 옮기는데, 그럼 survivor에는 용량 제한이 없는건가?



minor GC는 0.5초에서 1초정도밖에 안걸린다 -> 애플리케이션에 영향이 적음

반면 Major GC는 시간이 오래걸린다 거의 10배 이상 차이남

Stop-The-World 문제가 발생하기 때문에 GC 알고리즘에 대한 발전이 이뤄졌다.



1. Serial GC

   가장 단순한 GC

   실무에서 사용안함 -> CPU 코어 1개일 때 사용

2. Parallel GC

   Java8의 Default GC

   MinorGC는 멀티쓰레드로 수행

   Old는 싱글

3. Parallel Old GC

   2번 개선

   Old도 멀티 쓰레도 수행

   Mark Summary Compact 이용

4. Concurrent Mark Sweep GC

   앱 쓰레드와 GC 스레드가 동시에 실행되어 StopTheWorld 시간을 최대한 줄임

   대신 GC 과정이 복잡함 -> CPU 사용량이 높다

   Java 9 에서 Deprecated, Java14에서 중지됨

5. Garbage First GC (G1 GC)

   jdk 7에서 release 되고, Java 9 버전부터 Default GC로 사용

   4GB 이상의 힙메모리 stop the world 시간이 0.5초정도 필요할 때 사용 -> Heap 너무 작으면 별로임

   Region으로 young/old와 완전히 새로운 개념

   메모리가 많이 차있는 영역을 우선적으로 GC 한다.

   Eden -> Survivor -> Old 로 순차적으로 이동했지만, G1 GC는 더 효율적이라고 생각하는 위치로 재할당한다.

6. Shenanadoah GC

   Java 12에 release

   강력한 Concurrency와 가벼운 GC 로직으로 Heap 사이즈에 영향 없이 일정한 Pause 시간이 소요됨

7. ZGC

   Java 15에 release

   힙 크기가 증가하더라도 stop-the-world의 시간이 절대 10ms를 넘지 않는다.