Transaction의 옵션은 몇가지가 있는데 그 중 readOnly를 알아보려고 한다.

> This just serves as a hint for the actual transaction subsystem; it will *not necessarily* cause failure of write access attempts. A transaction manager which cannot interpret the read-only hint will *not* throw an exception when asked for a read-only transaction but rather silently ignore the hint.



https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/transaction/annotation/Transactional.html

공식 문서에 따르면 이 옵션은 읽기 전용 힌트를 제공한다고 한다. 기본적으로 Connection.setReadonly(true)를 호출한다. MySQL은 5.6.5 이상에서만 지원하고 h2는 지원하지 않는다.



JPA 구현체인 Hibernate을 사용하면 어떻게 될까?

Hibernate에서는 Session의 Flush Mode를 `FlushMode.MANUAL` 모드로 설정한다. 해당 트랜잭션은 커밋 시 flush를 하지 않는다는 것을 의미한다.

Hibernate는 Entity에 flush를 호출하지 않고 변경이 일어나도 무시된다. 또한 Dirty Checking을 하지 않기 때문에 Entity와 Snapshot 비교 과정이 생략되어 성능적으로도 이점을 얻을 수 있다.