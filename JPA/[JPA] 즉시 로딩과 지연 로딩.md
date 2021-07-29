# 즉시 로딩과 지연 로딩



### 연관관계 매핑

Member를 조회할 때 Team도 함께 조회해야 할까?


### @Mapping(fetch=fetchType.LAZY) 설정을 통해 지연로딩

![](https://images.velog.io/images/mohai2618/post/35f2f8f2-57dd-4bcf-ba7c-343f0565dd2d/image.png)

### @Mapping(fetch=fetchType.EAGER) 설정을 통해 즉시로딩
![](https://images.velog.io/images/mohai2618/post/051203ca-979e-4a79-abaf-339f689793d3/image.png)


## 프록시와 즉시로딩 주의
- 가급적 지연로딩만 사용(특히 실무에서)
- 즉시 로딩을 적용하면 예상치못한 SQL이 발생
- 즉시 로딩은 JPQL에서 N+1 문제를 일으킨다.
- @ManyToOne, @OneToOne은 기본이 즉시로딩 -> LAZY로 설정
- @OneToMany, @ManyToMany는 기본이 지연 로딩

## 지연 로딩 활용 -실무
- 모든 연관관계에 지연 로딩을 사용해라!
- 실무에서 즉시 로딩을 사용하지 마랒!
- JPQL fetch 조인이나, 엔티티 그래프 기능을 사용해라!
- 즉시 로딩은 상상하지 못한 쿼리가 나간다.