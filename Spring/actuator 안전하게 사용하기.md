# Spring Actuator 안전하게 사용하기

https://techblog.woowahan.com/9232/

# Spring Actuator란

Actuator는 외부 라이브러리로 의존성에 추가하면 바로 애플리케이션 모니터링 및 관리를 할 수 있습니다.

```yaml
# build.gradle 예시
dependencies {
    implementation 'org.springframework.boot:spring-boot-starter-actuator'
}
```

Health Check 용도의 actuator health endpoint입니다.

# Actuator 보안 이슈

간편하게 사용할 수 있지만 환경변수 값, 내부의 정보를 외부로 유출하거나 서비스를 강제로 중단시키는 경우가 발생할 수 있습니다.

따라서 불필요한 endpoint를 비활성화시켜서 해당 문제에 대해 방지해야합니다.

대표적으로 누락되는 상황입니다.

## 1. 환경변수로 중요 정보를 저장해 둔 경우

소스코드가 유출될 수 있기 때문에 소스코드에 api key, db password와 같은 중요 정보를 하드코딩 하지 않도록 권고합니다. 하지만 개발하는 입장에서 해당 정보를 계속 사용해야하기 때문에 보통 환경변수를 주입 받아서 활용하도록 구현합니다.

이때 만약 Spring Actuator의 env endpoint가 enable 되어있고 expose 되어있다면 서비스에 사용 중인 환경 변수를 볼 수 있기 때문에 유출이 가능합니다.

https://docs.spring.io/spring-boot/docs/current/actuator-api/htmlsingle/#env.entire

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/461f5a00-c0ef-419a-aca8-0f40ab78f499/Untitled.png)

## 2. 중요 정보가 메모리에 올라가 있는 경우

서비스 운영 중 사용한 중요 정보가 아직 메모리에 남아있느 경우 heapdump를 통해 해당 내용을 전부 받아올 수 있습니다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5115270b-60a5-42cc-b6cc-5032df38984b/Untitled.png)

이런식으로 웹 애플리케이션의 heapdump를 받아와서 사용하고 있는 application.yml의 정보를 받아올 수 있습니다.

https://docs.spring.io/spring-boot/docs/current/actuator-api/htmlsingle/#heapdump

## 3. Shutdown endpoint를 enable/expose 한 경우

만약 shutdown endpoint가 활성화 되어 있는 경우 임의로 웹 애플리케이션을 중지시켜버릴 수 있기 때문에 서비스 가용성에 문제가 발생할 수 있습니다.

https://docs.spring.io/spring-boot/docs/current/actuator-api/htmlsingle/#shutdown

현재 저희 ep 수집기 쪽 shutdown이 enabled로 되어있는거로 보여져서 확인 필요

# Spring Actuator를 안전하게 사용하는 방법

- Actuator endPoint는 전부 disable한 상태로 필요한 것만 추가하여 화이트 리스트 형대로 운영한다.
- endPoint expose가 필요한 경우, 꼭 필요한 것만 include하여 화이트리스트 형태로 운영한다 또한 asterisk(*)를 이용하여 include하지 않는다.
- shutdown endpoint는 enable하지 않는다.
- JMX형태로 Actuator 사용이 필요하지 않는 경우 disable 한다.
- Actuator는 서비스 운영에 사용되는 포트와 다른 포트를 사용한다.
- Actuator에 접근할 때에는, 인증된 사용자만 접근 가능하도록 제어한다.