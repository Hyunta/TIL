ThreadLocal은 쓰레드 별로 데이터를 적재한다. 그래서 당연히 Stack 영역을 사용하나? 생각했는데 JVM Memory에서 Stack 영역은 primitive type와 객체 참조값을 보관한다고 알고 있다. 그래서 Heap 영역을 사용한다고 추측했다.

ThreadLocal은 실제로 heap 영역에 저장된다고 한다. `ThreadLocalMap` 이라는 객체를 만들어서 thread와 threadLocal을 담는다. 따라서 이 맵을 힙이 가지고 있는다.



그럼 왜 스택이 아닌 힙을 선택해야하는가?

우선 Map, Object 형태라서 어쩔 수 없다 Heap에 저장되어야 한다. 그리고 gc에 의해서 관리되어질 수 있다.

만약 Stack에 저장되어있다면 method나 정의된 block에서만 사용할 수 있다. 해당 메서드나 block이 끝나면 객체가 소멸할 것이고 사라질 것이다. 그리고 여러 메서드에서 해당 값을 참조할 수 있기 때문에 Heap에 있어야 한다.