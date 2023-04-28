트랜잭션 격리 수준을 RepeatableRead로 해놨을 때 PhantomRead가 발생하는데 이를 해결하기 위해 대부분의 DB들은 MVCC를 사용한다.

- MySQL은 이전 커밋시점까지의 데이터를 읽어와서 해결한다
- PostgreSQL에서는 Rollback 시켜서 데이터를 저장하지 않는다.

