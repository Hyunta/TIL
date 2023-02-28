ChunkOrientedTasklet에서 Reader와 Writer는 필수 요소입니다. Processor는 없어도 ChunkOrientedTasklet은 구성할 수 있습니다.

# ItemWriter

ItemWriter는 Spring Batch에서 사용되는 출력 기능입니다.

Spring Batch가 처음 나왔을 때는 Item을 하나씩 다뤘습니다, 그러나 Spring Batch2와 청크 기반 처리의 도입으로 인해 ItemWriter에도 큰 변화가 있었습니다.

업데이트 이후로 ItemWriter는 Item 하나를 작성하지 않고 Chunk 단위로 묶인 ItemList를 다룹니다.

# Database Writer

Java 세계에서는 Jdbc or ORM을 사용해 RDBMS에 접근합니다.

Spring Batch에서는 JDBC와 ORM 모두 Writer를 제공합니다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4b30c04b-36c2-477e-ad78-1d19ddd472f2/Untitled.png)

Writer는 Chunk 단위의 마지막 단계이기 때문에 항상 마지막에 Flush를 해줘야만 합니다.

Writer가 받은 모든 item을 처리되면, Spring Batch는 현재 트랜잭션을 커밋합니다.

# JdbcBatchItemWriter

ORM을 사용하지 않는 경우 Writer는 대부분 JdbcBatchItemWriter를 사용합니다.

이 JdbcBatchItemWriter는 아래 그림처럼 한번에 DB로 전달하여 내부에서 쿼리들이 실행되도록 합니다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1f9f111b-e0c8-43da-b243-4d56f6d6c41d/Untitled.png)

이렇게 처리하게 되면 어플리케이션과 데이터베이스 간에 데이터를 주고 받는 회수를 최소화 하여 성능을 향상시킬 수 있습니다.