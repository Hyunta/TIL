# 객체지향 쿼리 언어(JPQL)



## 객체지향 쿼리 언어 소개

- JPQL
- JPA Criteria
- QueryDSL
- 네이티브 SQL
- JDBC API 직접 사용, MyBatis, SpringJdbcTemplate 함께 사용

----

가장 단순한 조회 방법

- EntityManager.find()
- 객체 그래프 탐색(a.getB().getC())

##### 만약 나이가 18이상인 회원을 모두 검색하고 싶다면?

### JPQL

- JPA를 사용하면 엔티티 객체를 중심으로 개발
- 문제는 검색 쿼리
- 검색을 할 때도 테이블이 아닌 엔티티 객체를 대상으로 검색
- 모든 DB 데이터를 객체로 변환해서 검색하는 것은 불가능
- 애플리케이션이 필요한 데이터만 DB에서 불러오려면 결국 검색 조건이 포함된 SQL이 필요

- JPA는 SQL을 추상화한 JPQL이라는 객체 지향 쿼리 언어 제공
- SQL과 문법 유사, SELCT, FROM, WHERE, GROUP BY, HAVING ,JOIN 지원
- JPQL은 엔티티 객체를 대상으로 쿼리
- SQL은 데이터베이스 테이블을 대상으로 쿼리

----

### Criteria

장점:

- 문자가 아닌 자바 코드로 JPQL을 작성할 수 있음.

단점:

- JPA 표준이긴 하나 유지 보수 힘듬
- 코드의 가독성이 떨어짐



#### Criteria 대신 QueryDSL을 사용해라

----

### QueryDSL(오픈소스)

- 동적 쿼리 작성이 편리함
- JPQL 빌더 역할
- 컴파일 시점에 문법 오류를 찾을  수 있음
- 단순하고 쉬움 -> 실무사용권장

----

### Native SQL

- JPA가 제공하는 SQL을 직접 사용하는 기능
- ex) 오라클 CONNECT BY, 특정 DB만 사용하는 SQL 힌트





----

# JPQL

##### JPQL은 객체지향 쿼리 언어다.따라서 테이블을 대상으로 쿼리 하는 것이 아니라 엔티티 객체를 대상으로 쿼리한다.



## JPQL 문법

- select m from Members as  m where m.age > 18
- 엔티티와 속성은 대소문자 구분 O (Member, age)
- JPQL 키워드는 대소문자 구분 X (SELECT, FROM, Where)
- 엔티티 이름 사용, 테이블 이름이 아님 (Member)
- 별칭은 필수 (m) , as는 생략 가능



### 집합과 정렬

- ANSI Spec 모두 지원
  - COUNT, SUM, AVG, MAX, MIN
  - GROUP BY, HAVING
  - ORDER BY



### TypeQuery, Query

- TypeQuery : 반환 타입이 명확할 때 사용
- Query: 반환 타입이 명확하지 않을 때 사용

----

### 결과 조회 API

- query.getResultList() : 결과가 하나 이상일 때, 리스트 반환
  - 결과가 없으면 빈 리스트 반환
- query.getSingleResult() : 결과가 정확히 하나, 단일 객체 반환
  - 결과가 없으면 : javax.persistnece.NoResultException
  - 둘 이상이면: javax.persistence.NonUniqueResultException



### 파라미터 바인딩 - 이름 기준, (위치기준 - 사용x)

```java
//이름기준
SELECT m FROM Member m where m.username=:username  query.setParameter("username", usernameParam);


//위치기준
SELECT m FROM Member m where m.username=?1 
query.setParameter(1, usernameParam);
--> 나중에 추가가 됐을 때 변경해줘야함. 번거로움 사용X
```



----

## 프로젝션

SELECT 절에 조회할 대상을 지정하는 것

- 프로젝션 대상: 엔티티, 임베디드 타입, 스칼라 타입(숫자, 문자등 기본 데이터 타입)

``` java
SELECT m FROM Member m -> 엔티티 프로젝션
SELECT m.team FROM Member m -> 엔티티 프로젝션
SELECT m.address FROM Member m -> 임베디드 타입 프로젝션(엔티티 필요)
SELECT m.username, m.age FROM Member m -> 스칼라 타입 프로젝션 DISTINCT로 중복 제거

```



### 여러 값 조회

`SELECT m.username, m.age From Member m`

1. Query 타입으로 조회
2. Object[] 타입으로 조회
3. new 명령어로 조회
   - 단순 값을 DTO로 바로 조회
   - 패키지 명을 포함한 전체 클래스 명 입력

`SELECT new jpabook.jpql.UserDTO(m.username, m.age) From Member m`

​			

----

## 페이징 API

- JPA는 페이징을 다음 두 API로 추상화
  - setFirstResult(int startPosition) : 조회 시작 위치 (0부터 시작) 
  - setMaxResults(int maxResult) : 조회할 데이터 수



----

## 조인

- INNERJOIN:
  - SELECT m FROM Member m [INNER] JOIN m.team t
- OUTERJOIN:
  - SELECT m FROM Member m LEFT [OUTER] JOIN m.team t 
- 세타 조인:
  - select count(m) from Member m, Team t where m.username  = t.name



### ON 절

1. 조인 대상 필터링

   - ex) 회원과 팀을 조인하면서, 팀 이름이 A인 팀만 조인

   - JPQL:

     SELECT m, t FROM Member m LEFT JOIN m.team t on t.name = 'A'  

   - SQL:

     SELECT m.*, t.* FROM  Member m LEFT JOIN Team t ON m.TEAM_ID=t.id and t.name='A'

     

2. 연관관계 없는 엔티티 외부 조인(하이버네이트 5.1부터)

   - 예) 회원의 이름과 팀의 이름이 같은 대상 외부 조인

   - JPQL: 

     SELECT m, t FROM Member m LEFT JOIN Team t on m.username = t.name 

   - SQL: 

     SELECT m.*, t.* FROM  Member m LEFT JOIN Team t ON m.username = t.name



----

## 서브 쿼리

- 나이가 평균보다 많은 회원 

  select m from Member m where m.age > (select avg(m2.age) from Member m2)  

- 한 건이라도 주문한 고객 

  select m from Member m where (select count(o) from Order o where m = o.member) > 0 

-------------------------

# 210806 일시정지



