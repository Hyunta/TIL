OneToMany 단방향이 안좋다고 주장하는 이유는?

- 엔티티가 관리하는 외래키가 다른 테이블이 있음 -> 혼란스러울 수 있음, 의도치않은 쿼리라 생각해서
- 연관관계 대상에 update 문이 발생
- join table 시 문제 발생