# 다양한 연관 매핑

## 목차

- 연관관계 매핑시 고려사항 3가지
- N:1
- 1:N
- 1:1
- N:M



## 연관관계 매핑시 고려사항 3가지

### 1. 다중성

- 다대일, 일대다, 일대일, 다대다
- @ManyToOne, @OneToMany, @OneToOne, @ManyToMany

#### 다대다는 실무에서 사용하면 안된다!



### 2. 단방향, 양방향

- 테이블 (DB)
  - 외래 키 하나로 양쪽 조인 가능
  - 사실 방향이라는 개념이 없음
- 객체 (Java)
  - 참조용 필드가 있는 쪽으로만 참조 가능
  - 한쪽만 참조하면 단방향
  - 양쪽이 서로 참조하면 양방향
    - 양방향 == 단방향 2개가 존재 따라서 **주인**을 정해야함



### 3. 연관관계의 주인

- 테이블은 외래 키 하나로 두 테이블이 연관관계를 맺음
- 객체 양방향 관계는 참조가 2군데 있어서 주인을 정해야함
- 연관관계의 주인: 외래 키를 관리하는 참조
- 주인의 반대편: 외래 키에 영향을 주지 않음, 단순 조회만 가능



## 다대일 [N:1]

![image-20210723155914647](C:\Users\mohai\AppData\Roaming\Typora\typora-user-images\image-20210723155914647.png)

![image-20210723160139697](C:\Users\mohai\AppData\Roaming\Typora\typora-user-images\image-20210723160139697.png)



- 외래키가 있는 객체를 주인으로 사용한다.



## 일대다[1:N]

## ![image-20210723160824021](C:\Users\mohai\AppData\Roaming\Typora\typora-user-images\image-20210723160824021.png)



- 연관관계의 주인이 1인 경우
- 표준스펙에서 제공하지만 권장하지 않는 모델 실무에서는 거의 가져가지 않음
  - Team Entity를 손댔는데 Member Table에 영향을 미친다.
- @JoinColumn을 꼭 사용해야함, 그렇지 않으면 조인 테이블 방식을 사용함(중간에 테이블을 하나 생성함)



일대다 양방향은 가능하지만 공식스펙X

- 읽기 전용 필드 @JoinColumn(Insertable=false, updatable=false)
- 다대일 양방향을 사용하자!



## 일대일 [1:1]

- 일대일 관계는 그 반대도 일대일
- 주 테이블이나 대상 테이블 중에 외래키 선택 가능
  - 주 테이블에 외래 키
  - 대상 테이블에 외래 키
- 외래 키에 데이터베이스 유니크 제약조건 추가

![image-20210723165335319](C:\Users\mohai\AppData\Roaming\Typora\typora-user-images\image-20210723165335319.png)

![image-20210723165504611](C:\Users\mohai\AppData\Roaming\Typora\typora-user-images\image-20210723165504611.png)

![image-20210723170550096](C:\Users\mohai\AppData\Roaming\Typora\typora-user-images\image-20210723170550096.png)



- 대상 테이블에 외래키 단방향 관계는 JPA 지원 X
- 일대일 주 테이블에 외래 키 양방향과 매핑 방법은 같음



### 일대일 정리

- 주테이블에 외래키
  - 객체지향 개발자 선호
  - JPA 매핑 편리
    - 장점: 주 테이블만 조회해도 대상 테이블에 데이터 확인 가능
    - 단점: 값이 없으면 외래 키에 null 허용
- 대상 테이블에 외래키
  - 대상 테이블에 외래 키가 존재
    - 장점: 주 테이블과 대상 테이블을 일대일에서 일대다로 바꿀 때 테이블 구조 유지
    - 단점: 프록시 기능의 한계로 지연 로딩으로 설정해도 항상 즉시 로딩됨





## 다대다[N:M]

### 실무에서 사용하면 안된다!

![image-20210723171528034](C:\Users\mohai\AppData\Roaming\Typora\typora-user-images\image-20210723171528034.png)

![image-20210723171709547](C:\Users\mohai\AppData\Roaming\Typora\typora-user-images\image-20210723171709547.png)

### 한계:

- 중간테이블을 조회만 하는 경우는 거의 없음
- 연결 테이블이 단순히 연결만 하고 끝나지 않음
- 주문시간, 수량 같은 데이터가 들어올 수 있음



### 극복:

- 연결 테이블용 엔티티 추가 (중간 테이블을 엔티티로 승격)
- @ManyToMany -> @OneToMany, @ManyToOne

![image-20210723172456934](C:\Users\mohai\AppData\Roaming\Typora\typora-user-images\image-20210723172456934.png)











