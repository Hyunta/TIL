# [JAVA] Garbage Collection



## 가비지 컬렉션 과정 -Generational Garbage Collection

- 'stop-the-world' : GC 실행을 위해 JVM이 애플리케이션 실행을 멈추는 것, GC를 실행하는 쓰레드를 제외한 나머지 쓰레드를 모두 정지
- GC 튜닝 = stop-the-world 의 시간을 줄이는 것



- Java에서는 개발자가 프로그램 코드로 메모리를 명시적으로 해제하지 않기 때문에 GC가 더 이상 필요없는 (쓰레기) 객체를 찾아 지우는 작업을 한다. 
- 가비지를 컬렉터는 두가지 조건에 의해 만들어진다.



Weak Generational Hypothesis

1. 대부분의 객체는 금방 접근 불가능 상태가 된다.
2. 오래된 객체에서 젊은 객체로의 참조는 아주 적게 존재한다.



HotSpot VM에서는 크게 2개로 물리적 공간을 나누었다. (Young / Old)

- Young 영역:
  - 새롭게 생성한 객체의 대부분
  - 대부분의 객체가 금방 접근불가능
  - 위 영역에서 객체가 사라질때 : Minor GC
- Old 영역:
  - 접근 불가능 상태로 되지 않아 Young에서 살아남은 객체 복사
  - 대부분 Young보다 크게 할당
  - 위 영역에서 객체가 사라질 때: Major GC(Full GC)

