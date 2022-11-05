OneToOne에는 Lazy Loading이 잘 작동하지 않는다.

1. Null값이 가능한 OneToOne의경우 프록시 객체로 감쌀 수 없기 때문이다.
2. 프록시 객체를 넣는다면, null이 아니라 프록시를 리턴하는 상태가 되버린다.
3. Jpa는 기본적으로 OneToOne에서 LazyLoading을 허용하지 않고, 즉시 값을 읽는다.

연관관계의 주인을 조회할 때는 LAZY가 되는데, 반대에서 조회할 때는 항상 Eager로 작동한다.