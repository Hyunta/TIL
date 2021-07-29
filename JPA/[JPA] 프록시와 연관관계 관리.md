# 프록시와 연관관계 관리



### 문제상황:

member 테이블에서 member.username을 받아오기만 할 때 자연스럽게 연관매핑된 Team 테이블의 정보도 받아온다면 자원 낭비.

JPA는 프록시와 지연로딩으로 해결한다.



### 프록시 기초:

- em.find() vs em.getReference()
- em.getReference(): 데이터베이스 조회를 미루는 가짜(프록시) 엔티티 객체 조회

![](https://images.velog.io/images/mohai2618/post/13cd5335-fce0-4c96-87b7-ed33d7a52c03/image.png)

프록시 클래스는 껍데기는 같지만 내용물은 없다



### 프록시 특징:

![](https://images.velog.io/images/mohai2618/post/48fe004b-531e-4935-98b7-24ae826e4a61/image.png)

- 프록시 객체는 실제 객체의 참조(Target)를 보관

![](https://images.velog.io/images/mohai2618/post/1ca3f3c9-1b07-4c45-9149-f29509003baa/image.png)

프록시에 데이터를 요청했을 때 진짜 값을 테이블을 요청하게 된다.



- 프록시 객체는 처음 사용할 때 한 번만 초기화
- 프록시 객체를 초기화 할 때, 프록시 객체가 실제 엔티티로 바뀌는 것은 아님, 초기화되면 프록시 객체를 통해서 실제 엔티티에 접근 가능
- 프록시 객체는 원본 엔티티를 상속받음, 따라서 타입 체크시 주의해야함 
  - (==비교 실패, 대신 instance of 사용)
- 영속성 컨텍스트에 찾는 엔티티가 이미 있으면 em.getReference()를 호출해도 실제 엔티티 반환
- 영속성 컨텍스트의 도움을 받을 수 없는 준영속 상태일 때, 프록시를 초기화하면
문제 발생
(하이버네이트는 org.hibernate.LazyInitializationException 예외를 터트림)


### 프록시 확인:
- 프록시 인스턴스의 초기화 여부 확인
PersistenceUnitUtil.isLoaded(Object entity) 
- 프록시 클래스 확인 방법:
entity.getClass().getName() 출력
(..javasist.. or HibernateProxy…)
- 프록시 강제 초기화:
org.hibernate.Hibernate.initialize(entity);