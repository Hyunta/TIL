# Zipkin

Microservice 분산 추적

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3b7bc861-7bd1-4221-9135-c51dfde4a5f2/Untitled.png)

하나의 요청에 발생하는 TraceId로 관리되고 각각의 서비스에서는 Span으로 작동한다.

## Spring Cloud Sleuth

- 해당 기술을 통해 zipkin과 연동이 가능하다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f999a4f0-dceb-4e02-b7aa-b600b138977d/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d2b38933-49db-4816-b9cc-30d9e91dfdff/Untitled.png)

- Span 각각의 서비스에서 트랜잭션에 대응하기 위해서 부여한다.