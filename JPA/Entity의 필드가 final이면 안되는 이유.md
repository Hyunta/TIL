Java에서 Entity를 만들 때 필드값을 final로 지정하지 않았다.

이 이유가 setter를 통해서 값을 주입해줘야되기 때문에 프록시로 관리되어져야해서 라고 생각했다.

그런데 Kotlin에서는 val로 필드값을 갖고 있을 수 있어서 궁금해서 다시 찾아봤다.



# JPA Entity 규칙

1. 엔티티는 무조건 protected 이상의 기본 생성자가 있어야 한다.
2. final이면 안된다. 메서드, 변수들도 모두 final이면 안된다.

https://download.oracle.com/otn-pub/jcp/persistence-2_1-fr-eval-spec/JavaPersistence.pdf?AuthParam=1680080705_d9ff32b740371a49a7b73e67d1d70009
