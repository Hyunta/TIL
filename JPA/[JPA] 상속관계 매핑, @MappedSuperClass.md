- 관계형 DB는 상속관계 X
- 슈퍼타입 서브타입 관계라는 모델링 기법이 객체 상속과 유사
- 상속관계 매핑:
  - 객체의 상속과 구조의 DB의 슈퍼타입 서브타입 관계를 매핑



##### 전략:

Join 전략, 단일 테이블 전략, 구현 클래스마다 테이블 전략



## 주요 Annotation

- @Inheritance(strategy= InheritanceType.XXX)
  - JOINED: 조인 전략
  - SINGLE_TABLE: 단일 테이블 전략
  - TABLE_PER_CLASS: 구현 클래스마다 테이블 전략



### 조인 전략(대부분 사용)
![](https://images.velog.io/images/mohai2618/post/a611077a-90c1-4cdb-93f8-57186cec297c/image.png)

- 장점:
  - 테이블 정규화
  - 외래 키 참조 무결성 제약조건 활용가능
  - 저장 공간 효율화
- 단점
  - 조회시 조인을 많이 사용, 성능 저하
  - 조회 쿼리가 복잡함
  - 데이터 저장시 INSERT SQL 2번 호출
    




### 단일 테이블 전략
![](https://images.velog.io/images/mohai2618/post/2231f74e-9c53-4301-8ffa-07bb31492ee1/image.png)

- 장점
  - 조인이 필요 없으므로 일반적으로 조회 성능이 빠름
  - 조회 쿼리가 단순함
- 단점
  - 자식 엔티티가 매핑한 컬럼은 모두 null 허용
  - 단일 테이블에 모든 것을 저장하므로 테이블이 커질 수 있다. 상황에 따라서 조회선능이 오히려 느려질 수 있다.

### 구현 클래스마다 테이블 전략
![](https://images.velog.io/images/mohai2618/post/fba9eb37-9cb1-4514-bbb2-14606dc7f53b/image.png)

#### 사용하면 안되는 전략!
DBA와 ORM 전문가 둘 다 추천하지 않는다, 서로 묶이는게 없기 때문에 예를 들어 정산을 해야하면 각 테이블 별로 정산을 해야한다.


- 장점:
  - 서브 타입을 명확하게 구분해서 처리할 때 효과적
  - not null 제약조건 사용가능
- 단점:
  - 여러 자식 테이블을 함께 조회할 때 성능이 느림(UNION SQL 필요)
  - 자식 테이블을 통합해서 쿼리하기 어려움



## @MappedSuperClass

![img](https://images.velog.io/images/mohai2618/post/e4e50106-596e-4979-a2ac-c8c0ef5173e5/image.png)

- 상속관계 매핑X
- 엔티티X, 테이블과 매핑X
- 부모 클래스를 상속 받는 자식 클래스에 매핑 정보만 제공
- 조회, 검색 불가 (em.find(BaseEntity) 불가능)
- 직접 생서해서 사용할 일이 없으므로 추상 클래스 권장
- 테이블과 관계 없고, 단순히 엔티티가 공통으로 사용하는 매핑 정보를 모으는 역할
- 주로 등록일, 수정일, 등록자, 수정자 같은 전체 엔티티에서 공통으로 적용하는 정보를 모을 때 사용
- 참고: @Entity 클래스는 엔티티나 @MappedSuperClass로 지정한 클래스만 상속 가능