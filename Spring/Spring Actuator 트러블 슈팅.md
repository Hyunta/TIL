# 3. SpringBoot Actuator 설정

1. Actuator 관련하여 기능을 설정한다.
   - 포트번호 변경
   - endpoint를 모두 disable
   - jmx 관련 exposure 모두 제거
   - web 필요한 endpoints exposure 추가 및 enable

```yaml
management:
  server:
    port: 8081
  endpoints:
    enabled-by-default: false
    jmx:
      exposure:
        exclude: "*"
    web:
      exposure:
        include: "info,health,prometheus"
  endpoint:
    info:
      enabled: true
    health:
      enabled: true
    prometheus:
      enabled: true
```

## 트러블 슈팅

해당 내용을 반영해서 배포했는데, 아래와 같은 에러 발생

```bash
2023-02-27 17:53:11.326 ERROR 13404 --- [           main] o.s.boot.SpringApplication               : Application run failed

java.lang.IllegalStateException: java.lang.IllegalStateException: Logback configuration error detected:
ERROR in ch.qos.logback.core.rolling.RollingFileAppender[FILE] - Failed to create parent directories for 
```

eureka 관련된 설정 다 지우고 나니 해결됨

- /actuator/prometheus에서 정보를 못받아옴